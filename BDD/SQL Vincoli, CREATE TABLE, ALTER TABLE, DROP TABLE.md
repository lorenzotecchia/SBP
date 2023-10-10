---
author: Simone Parente
---
- Indice
# Structured Query Language

- Linguaggio che permette di definire, manipolare e gestire basi di dati
- Fornisce statement per manipolazione/definizione di dati, può essere usato interattivamente(?) o essere embedded in altri programmi e altri linguaggi
- Notazioni
    
    Relazione $\xrightarrow{}$ Tabella
    
    Tupla $\xrightarrow{}$ Riga
    
    Attributo $\xrightarrow{}$ Colonna
    

## Definizione di dati, schemi e vincoli SQL

---

Uno schema è utilizzato per raggruppare tabelle e costrutti appartenenti alla stessa applicazione di database. Ogni schema ha un nome e dei descrittori per ogni elemento dello schema. Include inoltre:

- Tabelle
- Domini

- Viste
- Altri costrutti (funzioni, procedure, ecc.)

`CREATE TABLE nome_tabella;` è usato per specificare una nuova relazione, a cui si può assegnare un nome e un insieme di attributi e vincoli. Gli attributi vengono specificati da:

- Nome
- Tipo di dato
- Eventuali vincoli
- Specifica delle chiavi (primarie o esterne)
- Vincoli di integrità di entità
- Vincoli di integrità referenziale

# Tipi di dati

---

- Numerici
    - Interi
        - `INTEGER`, `INT`, `SMALLINT`
    - Reali
        - `FLOAT`, `REAL`, `DOUBLE PRECISION`
    - Numeri formattati
        - `DECIMAL(i,j)`, `DEC(i,j)`, `NUMERIC(i,j)`
            - i (precisione), indica il numero di cifre decimali
            - j (scala), indica il numero di cifre dopo la virgola
- Stringhe
    - `CHAR(n)`, `CHARACTER(n)`
    - `VARCHAR(n)` o `CHAR VARYING(n)`
- Stringhe di bit
    - A lunghezza fissa
        - `BIT(n)`
    - A lunghezza variabile
        - `BIT VARYING(n)`
- `DATE`
    - Con componenti YEAR, MONTH, DAY
        - Formato YYYY-MM-DD
- `TIME`
    - Ha come componenti HOUR, MINUTE, SECOND
        - Formato HH:MM:SS
- È possibile creare domini personalizzati
    
    ```sql
    CREATE DOMAIN SSN_TYPE AS CHAR(9);
    ```
    

# Vincoli

---

>[!tip] Vincolo: condizione che deve essere rispettata


## Vincoli su valori `NULL` o predefiniti

---

Per impedire che un attributo possa avere valore `NULL` si usa il vincolo `NOT NULL`. (specificato di default per la chiave primaria)
Per specificare un valore di default si usa `DEFAULT`, in caso non ci fosse questa clausola, il valore di default sarà NULL.

## Vincoli sulle tuple

---

Il vincolo `CHECK` serve a controllare che un attributo rispetti determinate condizioni.

`CHECK(vincolo)`

- Esempi
    
    ```sql
    CREATE DOMAIN sesso AS CHAR
    	CHECK (sesso='m' OR sesso='f');
    ```
    
    ```sql
    CREATE DOMAIN voto AS SMALLINT
    	CHECK (voto>0 AND voto<=30);
    ```
    

## Vincoli di chiave

---

I vincoli di chiave sono aggiunti di solito all’interno delle istruzioni `CREATE TABLE`

- Esempi
    
    Per chiavi date da attributi singoli:
    
    ```sql
    CREATE TABLE Persona
    	Nome VARCHAR(20),
    	Cognome VARCHAR(20),
    	CodiceFiscale VARCHAR(16),
    CONSTRAINT Persona_PK PRIMARY KEY(CodiceFiscale);
    ```
    
    Per chiavi date da attributi composti:
    
    ```sql
    CREATE TABLE Persona
    	Nome VARCHAR(20),
    	Cognome VARCHAR(20),
    	DataNascita DATE;
    CONSTRAINT Persona_PK PRIMARY KEY(Nome, Cognome, DataNascita);
    ```
    

## Vincoli di unicità

---

È possibile definire vincoli di chiave alternativa, il vincolo `UNIQUE` specifica una chiave secondaria (stessa sintassi di chiave primaria)

```sql
CREATE TABLE Persona
	Nome VARCHAR(20),
	Cognome VARCHAR(20),
	CodiceFiscale VARCHAR(16),
CONSTRAINT Persona_PK PRIMARY KEY(Nome, Cognome, DataNascita),
CONSTRAINT Persona_UNIQUE UNIQUE(CodiceFiscale);
```

## Vincoli integrità referenziale

---

Si può specificare una chiave esterna tramite la keyword `FOREIGN KEY` seguito dall’attributo che indica la chiave esterna, la parola `REFERENCES(attributo esterno)`

L’azione referenziale “triggerata” può essere specificata nella clausola `FOREIGN KEY`.

```sql
CREATE TABLE Indirizzo
	Via VARCHAR(20),
	Citta VARCHAR(20),
	Provincia VARCHAR(20),
	CAP VARCHAR(5),
	CFIntestatario VARCHAR(16),
CONSTRAINT Indirizzo_PK PRIMARY KEY(Via, Citta, Provincia, CAP),
CONSTRAINT Indirizzo_FK FOREIGN KEY(CFIntestatario ) REFERENCES Persona(CodiceFiscale);
```

# Comando DROP

---

Quando uno schema o una tabella non sono più necessari si usano rispettivamente i comandi:

## `DROP SCHEMA`

---

## `DROP TABLE`

---

## `CASCADE`

---

Elimina lo schema, le tabelle, i domini e tutti gli altri elementi

## `RESTRICT`

---

Elimina lo schema e tutti gli altri elementi solo se lo schema è vuoto

## `CASCADE`

---

Viene eliminata la tabella, i vincoli, le viste, ecc.

## `RESTRICT`

---

La tabella viene eliminata solo se non è referenziata in alcun vincolo o vista

---

# Comando ALTER TABLE

---

Si utilizza per modificare le tabelle

- Aggiunta o rimozione di attributi
- Cambio di definizione di una colonna
- Aggiunta o rimozione di un vincolo

Il valore di default può essere specificato, in caso contrario sarà `NULL`, la clausola `NOT NULL` non è permessa con questo comando

- Esempio
    - Aggiungere un attributo età all’interno della tabella Persona
    
    ```sql
    ALTER TABLE Persona
    ADD Eta INTEGER;
    ```
    

## Comando INSERT INTO

<aside>
💡 Serve per inserire dei valori nella tabella

</aside>

---

```sql
INSERT INTO dipartimento(nomedip, numero)
VALUES  ('dieti',1), ('legge',2), ('economia',3)
```

```sql
INSERT INTO impiegato(cf,cognome,nome,numero_dipartimento)
VALUES ('abcdefghilmnopqr','francesco','tavano',2), 
				('abcdefghilmnopqr','francesco2','tavano',1), 
				('abcdefghilmnopqr','francesco3','tavano',3)
```

## Comando CREATE VIEW

---

Le relazioni create con `CREATE TABLE` sono tabelle/relazioni base in SQL, create e memorizzate come file dal DBMS.

Le relazioni virtuali vengono create con `CREATE VIEW`, cui può corrispondere o meno un file fisico.

Gli attributi sono in ordine di inserimento.

- Esempio
    
    Supponiamo di avere una tabella
    
    ```diff
    +------------+-----------+----------+---------+
    | EmployeeID | FirstName | LastName | Salary  |
    +------------+-----------+----------+---------+
    | 1          | John      | Doe      | 50000   |
    | 2          | Jane      | Smith    | 60000   |
    | 3          | Mike      | Johnson  | 55000   |
    +------------+-----------+----------+---------+
    ```
    
    E vogliamo creare una vista che mostri solo i dipendenti con uno stipendio maggiore di 55000. La vista può essere creata come segue:
    
    ```sql
    CREATE VIEW HighPaidEmployees AS
    SELECT EmployeeID, FirstName, LastName, Salary
    FROM Employee
    WHERE Salary > 55000;
    ```
    
    Con questa istruzione, stiamo creando una vista chiamata "HighPaidEmployees" che seleziona solo le righe dalla tabella "Employee" dove lo stipendio è maggiore di 55000.