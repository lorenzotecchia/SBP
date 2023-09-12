---
Date: November 8, 2022
Number: 17
Reviewed: Yes
Status: Done
author: Simone Parente Martone
---
# Dove annidare le query

---

SELECT      NO
FROM        SI
WHERE       SI
GROUP BY    NO
HAVING      SI
ORDER BY    NO

---

- Esempio di query annidata e ragionamento alla base
    
    Dato lo schema logico:
    STUDENTE(Matricola, Nome, Cognome)
    ESAME(Matricola, Corso)
    
    Per trovare tutti gli studenti che hanno sostenuto tutti gli esami che ha sostenuto anche lo studente con matricola 100 ragiono in questo modo:
    
    Trovo gli studenti che hanno sostenuto almeno tutti gli esami sostenuti dallo studente con matricola 100
    Trovo tutti gli studenti per cui NON ESISTA un esame che hanno sostenuto e che lo studente 100 non abbia sostenuto
    L’insieme degli esami sostenuti dallo studente 100 e non sostenuti dallo studente x è vuoto
    
    ```sql
    SELECT *           --Insieme degli studenti S per cui l'insieme degli esami sostenuti da 100, ma non da S è vuoto
    FROM Studenti AS S
    WHERE NOT EXISTS
    (
    	SELECT E.Corso --Insieme dei corsi sostenuti da 100 e
    	FROM Esami AS E --dallo studente S.Matricola
    	WHERE E.Matricola='100' AND E.Corso NOT IN
    		(
    			SELECT E2.Corso
    			FROM ESAMI AS E2
    			WHERE E2.Matricola=S.Matricola
    		) --Insieme dei corsi sostenuti dallo studente S.Matricola
    )
    ```

# Vincoli e Assertion
---
Esistono dei vincoli diversi da quelli visti in precedenza (cioè quelli su valori null, sulle tuple, su domini di attributi, vincoli di chiave, di integrità referenziale) che sono chiamati vincoli di identità semantica e non sono comuni a tutte le basi di dati e devono essere specificati in maniera differente da quelli che già conosciamo.

## Vincoli di base

---

```sql
CONSTRAINT <nome_vincolo> <vincolo>
/*dove*/ <vincolo>:= CHECK <espressione booleana>
									 UNIQUE (<lista_attributi>)
									 PRIMARY KEY (<lista_attributi>)
									 FOREIGN KEY (<lista_attributi_FK>) REFERENCES (<nome_tabella>)(lista_att_PK)

<azione>:= NO ACTION | CASCADE | SET DEFAULT | SET NULL
```

## Vincoli di integrità semantica

---

Per i seguenti vincoli:

> Un impiegato non può guadagnare più del suo supervisore
> 

> Ad un progetto non possono lavorare più di n impiegati
> 

> Un impiegato non può lavorare per $>$ $48$ ore settimanali
> 

È possibile usare costrutti quali `ASSERTION` e `TRIGGER` per specificare questi vincoli

- All’interno di programmi applicativi

- Tramite un linguaggio di specifica dei vincoli

I vincoli possono essere di 4 tipi

1. Table-level constraints
    1. `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `CHECK`
2. Column-level constraints
    1. `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `CHECK`, `NOTNULL`
3. Schema-level constraints
    1. Ogni volta che la base di dati cambia stato, si controlla se questi vincoli siano stati o meno violati

## Vincoli intra-relazionali e inter-relazionali

---

<aside>
💡 Un vincolo è intra-relazionale se per verificare che esso sia rispettato è necessario controllare esclusivamente la tabella in cui è avvenuta la modifica.

La maggior parte dei vincoli sono intra-relazionali

- Esempi
    - `PRIMARY KEY`
    - `UNIQUE`
    - `NOT NULL`
    - `CHECK`
</aside>

<aside>
💡 Un vincolo è inter-relazionale se è necessario controllare diverse tabelle per verificare che esso sia stato o meno violato.

Un esempio di vincolo inter-relazionali è quello di integrità referenziale (`FOREIGN KEY`), in quanto esso va a controllare che il valore definito nell’attributo esista nella tabella di riferimento

</aside>

## Vincolo di `CHECK`

---

In teoria qualsiasi vincolo di tabella o colonna possono essere espressi tramite un vincolo di CHECK (non in PostgreSQL perché non possiamo creare subquery all’interno di vincoli di `CHECK`)

# Trigger


---

Qualcosa che viene lanciato all’accadere di un determinato evento

# `Assertion` (Schema-Level constraint)

---

Per evitare anomalie causate dai vincoli di check su più tabelle potremmo utilizzare le assertion, esse sono dei vincoli che appartengono direttamente allo schema di basi di dati (per questo sono detti Schema-Level). Ma queste ultime non sono implementate all’interno dei DBMS, nonostante questo uno degli esercizi dell’esame è la creazione di una Assertion.

```sql
CREATE ASSERTION <nome_assertion>
CHECK (condizione)
```

`<nome_assertion>` potrà essere utilizzato per modificare o eliminare l’assertion in futuro

```sql
CREATE ASSERTION <nome_assertion>
CHECK ([NOT] EXISTS(
												SELECT
												<cerco la condizione del vincolo>
											)
			)
```

- Esempi di assertion
    
    Dato lo schema fisico: (*******Primary Key*******, ***********************Foreign Key***********************)
    
    ALBERO*(CodAlbero, CodRadice)*
    
    NODE*(CodNodo, Label, **CodAlbero**)*
    
    ARCO*(CodArco, NodoSorgente, NodoTarget, Label, **CodAlbero**)*
    
    > Il NodoSorgente e il NodoTarget di un albero devono essere diversi
    > 
    
    Questo è un vincolo intra-relazionale, quindi non c’è bisogno di creare una assertion, bensì basta inserire un vincolo nella tabella
    
    ```sql
    ALTER TABLE ARCO
    ADD CONSTRAINT NodoS_NOT_NodoT CHECK NodoSorgente<>NodoTarget;
    ```
    
    ---
    
    > L’identificativo di una radice è un nodo dell’albero
    > 
    
    In questo caso il vincolo è inter-relazionale, quindi abbiamo bisogno di creare un’assertion
    
    ```sql
    CREATE ASSERTION CodR_NODE_CodA
    CHECK NOT EXISTS
    (
    	SELECT * 
    	FROM Albero AS A 
    	WHERE A.CodRadice NOT IN 
    		(
    			SELECT CodNodo
    			FROM Node AS N
    			WHERE N.CodNodo=T.CodRadice
    		)
    ```
    
    Altri vincoli inter-relazionali (da fare come esercizio)
    
    - Un nodo ha un solo padre
    - Una radice non ha padri
    - Tutti i nodi sono connessi