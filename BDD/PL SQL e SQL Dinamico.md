---
author: Simone Parente
---
# PL/SQL

Procedural Language for the Structured Query Language

---

Permette di spostare parte del carico computazionale sul server DBMS.

Ci permette di lavorare sui risultati di una query anche una riga alla volta e non necessita di convertire i tipi (`%type`, `%rowtype`).

## Struttura

---

Diviso in strutture (blocks) che possono essere

- Pure SQL
- PL/SQL (Procedural Language SQL)

```sql
[DECLARE]
declaration_statements

BEGIN

executable_statements

[EXCEPTION]
except_handling_statements

END;
```

`DECLARE` è opzionale e contiene le variabili che verranno utilizzate nel seguito del programma

`BEGIN`/`END` è il blocco che contiene tutte le istruzioni che saranno eseguite (istruzioni,cicli ecc.)

`EXCEPTION` è opzionale e contiene le istruzioni per gestire le exception

Ogni blocco termina con uno slash (/) (Non in PostgreSQL)

- Esempi ORACLE
    
    ```sql
    DECLARE
    message VARCHAR(100):='Hello, World!'
    BEGIN
    DBMS_OUTPUT.put_line(message);
    
    EXCEPTION
    	WHEN OTHERS --qualsiasi exception venisse lanciata
    	THEN        --verrà gestita così:
    	DBMS_OUTPUT.put_line(SQLERRM);
    
    END;
    ```
    
    ```sql
    DECLARE
    message VARCHAR2(100):='Hello'
    BEGIN
    	DECLARE
    		message2 VARCHAR2(100):= message||'World!';
    	BEGIN
    		DBMS_OUTPUT.put_line(l_message2);
    	END
    
    	EXCEPTION
    		WHEN OTHERS
    		THEN
    		DBMS_OUTPUT.put_line(DBMS_UTILITY.format_error_stack);
    END;
    ```
    
- Esempio PostgreSQL
    
    ```sql
    CREATE SCHEMA IF NOT EXISTS schemaprova; //Se lo schema "schemaprova" non esiste, lo creo, altrimenti salta questa operazione
    CREATE PROCEDURE schemaprova.prova() AS  //Creo la procedure di nome "prova" (procedure perché non ha valori di ritorno) all'interno dello schema
    $$                                       --"schemaprova"
    DECLARE //Blocco in cui si dichiarano eventuali variabili che utilizzeremo nel corpo della funzione/procedure
    message VARCHAR(100) :='Hello, World!'; //variabile "message" di tipo VARCHAR di massimo 100 caratteri inizializzata con una stringa
    BEGIN                                   //le stringhe si indicano con apici
        RAISE NOTICE '%', message;          //Stampa la variabile message. % è universale, vale per ogni tipo di variabile
    EXCEPTION //Blocco che contiene eventuali gestioni di Exceptions
    WHEN OTHERS //Con "OTHERS" si intendono tutte le altre Exceptions non gestite
    THEN
    RAISE EXCEPTION PLPGSQL_ERROR;
    END
    $$
    LANGUAGE plpgsql;
    
    CALL schemaprova.prova(); //chiamata di procedure in PLPGSQL
    //per le funzioni (che ritornano un valore) si usa SELECT nomeschema.nomefunzione(eventuali parametri)
    ```
    

## Blocchi con SQL

---

```sql
DECLARE
l_name employees.last_name%TYPE; 
BEGIN
	SELECT last_name INTO l_name
	FROM employees
	WHERE employee_id=138
END
```

- `l_name` è dichiarato dello stesso tipo del campo last_name nella tabella Employees
- Salva il campo last_name della table employees (dell'employee con id 138) nella variabile `l_name`

## Dichiarazione di variabili

---

```sql
DECLARE
part_number NUMBER(6); 
part_name VARCHAR(20);
in_stock BOOLEAN; 
part_price NUMBER(6,2)
BEGIN NULL;
END;
```

- `NUMBER` e `VARCHAR` sono SQL data types.
- `BOOLEAN` è un data type esclusivo di PL/SQL e PostgreSQL (Oracle non lo supporta)
- `NUMBER`(6,2) indica un numero con 6 digit complessivi, di cui 2 ***dopo la virgola***.

## Operazioni di `SELECT`

---

Una `SELECT` può ritornare:

Una singola riga:

Posso andare a recuperare i valori restituiti dichiarando in DECLARE le variabili restituite associandole all’output della SELECT tramite la keyword ********INTO********

Un insieme di righe:

Non so quante righe saranno restituite, necessiterò quindi di un cursore per scorrere la tabella  ottenuta.

Nessuna riga

## Costrutti condizionali

---

### Struttura

---

```sql
IF condition1 THEN
	statements1
ELSEIF condition2 THEN
	statements2
ELSE
	statements3
END IF;
```

- condition1 e condition2 sono espressioni booleane
- statements1, statements2 e statements3 sono istruzioni PL/SQL

### Esempio

---

```sql
BEGIN
    IF v_count>0 THEN
	    RAISE NOTICE 'v_count è positivo';
	    IF V_AREA>0 THEN
            RAISE NOTICE 'v_count e v_area sono positivi';
			END IF;
    ELSEIF v_count=0 THEN
        RAISE NOTICE 'v_count è uguale a 0';
    ELSE
        RAISE NOTICE 'v_count è negativo';
    END IF;
END
```

- Esempio 2
    
    ```sql
    IF salary BETWEEN 10000 AND 20000
    THEN
    give_bonus(employee_id,1000)
    ELSEIF salary>20000
    	THEN 
    		give_bonus(employee_id, 500);
    ELSE
    		give_bonus(employee_id, 0);
    END IF;
    
    ```
    

## Costrutti iterativi

---

1. *`FOR LOOP`* che cicla per un numero predeterminato di volte.
2. *`SIMPLE LOOP`* che viene eseguito fino a quando il ciclo non viene stoppato esplicitamente.
3. *`WHILE LOOP`* che cicla finché non si verifica una determinata condizione.

### *1. FOR LOOP*

---

Eseguito per un numero fisso di volte, specificando il `lower bound` (valore di partenza della variabile) e l’upper bound (valore finale della variabile) per la variabile di loop.

La variabile è incrementata/decerementata ogni volta che si fa un nuovo giro nel loop

```sql
FOR loop_variable IN [REVERSE] lower_bound..upper_bound LOOP
	statements
END LOOP;
```

- `loop_variable` è la variabile che regola il loop
- REVERSE indica se la variabile deve essere incrementata o decrementata ed è [opzionale]

```sql
FOR v_counter2 IN 1..5 LOOP
	DBMS_OUTPUT.PUT_LINE(v_counter2);
	END LOOP;
```

```sql
FOR v_counter2 IN REVERSE 5..1 LOOP
	RAISE NOTICE '%', prova
END LOOP;
```

### EXIT e EXIT WHEN

---

Per terminare il ciclo si può usare EXIT. Oppure EXIT WHEN nel caso in cui volessimo specificare una condizione per cui il ciclo dovrebbe terminare

```sql
v_counter:=0;
LOOP
	v_counter:=v_counter+1;
	EXIT WHEN v_counter=5;
END LOOP;
```

```sql
DO $$
 DECLARE
 i int :=0;
	 BEGIN
		LOOP
			i=i+1;
			raise notice '% ', i;
		EXIT WHEN i=5;
		END LOOP;
		END;
$$
```

### CONTINUE

---

```sql
v_counter:=0;
LOOP
--quando CONTINUE viene eseguito, il controllo torna qui
v_counter::=v_counter+1;
IF v_counter=3 THEN
	CONTINUE; --interrompe l'iterazione corrente a prescindere
END IF;
EXIT WHEN v_counter=5
```

```sql
DO $$
    DECLARE
        i int:=0;
        BEGIN
        LOOP
						//qui, quindi i verrà incrementato ancora di 1 (i==4) e "3" non verrà mai stampato
            i:=i+1; 
            raise notice '%', i;
            IF i=2 THEN
                raise notice 'i è 2'; //2 viene stampato dalla funzione precedente
                i:=i+1;               //incremento di 1 i e quindi i==3
                raise notice 'ora è 3';
                CONTINUE;             //il controllo dopo continue arriva

            END IF;
            EXIT WHEN i=10;
        END LOOP;
    END;
$$
```

### WHILE loop

---

## Struttura

---

```sql
WHILE condition
	statements
END LOOP;
```

## Oracle

---

```sql
v_counter:=0
WHILE v_counter>6 LOOP
	v_counter:=v_counter+1;
END LOOP
```

## PostgreSQL

---

```sql
DO
$$
    DECLARE
        i int:=0;
    BEGIN
        WHILE i<10 LOOP
            i:=i+1;
            raise notice 'i: %', i;
            end loop;
    END;
$$;
```

# Cursori

---

## Oracle VS PostgreSQL

```sql
DECLARE
**CURSOR** estrai_cognome **IS**
SELECT S.Nome, S.Matricola
FROM STUDENTI AS S
WHERE S.Cognome='Barra';
riga_corrente estrai_cognome**%ROWTYPE**
BEGIN
	OPEN estrai_cognome
	FETCH estrai_cognome INTO riga_corrente
	CLOSE estrai_cognome
END
```

```sql
DECLARE
	estrai_cognome **CURSOR FOR**
		SELECT S.Nome, S.Matricola
		FROM STUDENTI AS S
		WHERE S.Cognome='Barra';
	riga_corrente estrai_cognome**%TYPE**
BEGIN
	OPEN estrai_cognome
	FETCH estrai_cognome INTO riga_corrente
	CLOSE estrai_cognome
END
```

## Eccezioni

---

Le eccezioni sono utilizzate per gestire errori a **tempo di esecuzione** in statement PL/SQL.

Il blocco `EXCEPTION` è in carica di recuperare le exceptions e gestirle come (e se) specificato.

La keyword `OTHERS` si utilizza per gestire tutte le exceptions non precedentemente gestite.

# Procedure

<aside>
💡 Le procedure a differenza delle funzioni non hanno alcun valore di ritorno.

</aside>

---

## Struttura

```sql
CREATE [OR REPLACE] PROCEDURE procedure_name
[(parameter_name [IN | OUT | IN OUT] type [, ...])]
{IS | AS}
BEGIN
procedure_body
END procedure_name
```

- [] significa opzionale

- IN implica che il parametro può essere utilizzato nella procedure ma non può essere modificato (passaggio per valore) (maggior parte dei casi)
- OUT implica che a esso può essere assegnato un valore nella procedura ma non può essere utilizzato esternamente alla funzione (passaggio per riferimento)
- IN OUT implica che il parametro può essere utilizzato in lettura che scrittura

## Esempio

Questa procedura accetta 2 parametri in modalità IN, di conseguenza i valori dei due parametri dovranno essere impostati quando la procedura è chiamata (e non saranno modificabili nel corpo della procedura)

```sql
CREATE PROCEDURE update_product_price(
p_product_id IN produce.productsid%TYPE,
p_factor     IN NUMBER
)
AS
v_product_count INTEGER;
BEGIN
	--contiamo il numero di prodotti con l'ID dato
	--(se il prodotto esiste allora count==1)
	SELECT COUNT(*)
	INTO v_product_count
	FROM products
	WHERE product_id = p_product_id;
	
	--se il proodotto esiste(v_product_count=1) allora
	--aggiorna il prezzo del prodotto
	IF v_product_count=1 THEN
		UPDATE products
		SET price=price*p_factor
		WHERE product_id=p_product_id;
		COMMIT;
	END IF

EXCEPTION
	WHEN OTHERS THEN
		ROLLBACK;
END update_product_price;
/

```

- Non si può utilizzare una SELECT pura all’interno della procedura
    - o la si collega a un cursore
    - o si usa la keyword INTO
- Non si può utilizzare una SELECT per le query che restituiscono più di una riga

---

[9.4. String Functions and Operators](https://www.postgresql.org/docs/9.1/functions-string.html)

---

# SQL Dinamico

---

Consente di eseguire comandi SQL prodotti a runtime.

Le differenze principali con l’SQL statico è che in quest’ultimo la struttura del comando rimane la stessa, nell’SQL dinamico è l’intero comando ad essere prodotto a tempo di esecuzione

- Esempio
    
    ```sql
    CREATE PROCEDURE CANCELLA_TABELLA(table_name IN VARCHAR)
    AS
    		sql_istr VARCHAR(100);
    		BEGIN sql_istr:='DROP TABLE' || table_name;
    				EXECUTE IMMEDIATE(sql_istr);
    		EXCEPTION
    			gestione eccezioni;
    END;
    /
    ```
    

Modalità di interazione

1. La gestione dell’interrogazione avviene in due fasi
    1. `PREPARE` è il momento in cui si prepara il comando.
    2. `EXECUTE` in cui il comando viene mandato in esecuzione.
2. L’interrogazione può essere:
    1. eseguita immediatamente
    2. inserita in un parametro di tipo stringa che contiene il comando
    3. inserita in un comando specificato direttamente come parametro EXECUTE IMMEDIATE

### 1. Prepare and Execute

---

`PREPARE` analizza l’istruzione SQL e ne prepara una traduzione 

`PREPARE <nome_comando> FROM <comando SQL>`

dove `<nome_comando>` è il nome associato da `PREPARE` alla traduzione del comando SQL.

Il comando SQL può contenere parametri in ingresso rappresentati tramite `?`

```sql
PREPARE comandoSQL
FROM 'SELECT nome FROM studente WHERE matricola=?'
```

L’esecuzione del comando `PREPARE` associa alla variabile comandoSQL la traduzione dell’interrogazione, con un parametro in ingresso rappresentante la matricola dello studente. Dopodiché avviene l’esecuzione della query tramite il comando EXECUTE.

```sql
EXECUTE <nome_comando>[INTO variabiliTarget][USING <lista_parametri>]
```

Dove `<variabiliTarget>` contiene l’elenco di parametri in cui verrà scritto il risultato del comando

`<lista parametri>` specifica i valori da assegnare ai parametri variabili (per intenderci, i `?`)

- Esempio
    
    ```sql
    EXECUTE comandoSQL INTO nomeStudente USING matr_studente
    ```
    
    dove `matr_studente` è una variabile in cui è inserita la matricola studente N86001941 pertanto l’esecuzione del comando equivale a una query
    
    ```sql
    SELECT nome
    FROM studente
    WHERE matricola='N86001941'
    ```
    

### EXECUTE IMMEDIATE

---

In questa modalità la `PREPARE` non è eseguita esplicitamente con un apposito comando, verrà invece effettuata contestualmente alla preparazione.

### Struttura

---

```sql
EXECUTE IMMEDIATE <nome_comando>[INTO <listatarget][USING <listaPar>
--------------------------------------------------------------------
comandoSQL:=" DELETE FROM Studente WHERE Matricola = 'N86001941' ";
EXECUTE IMMADIATE comandoSQL;
```

### Esempio

```sql
DECLARE
sql_stmt    VARCHAR(200);
plsql_block VARCHAR(500);
emp_id      NUMBER(4):=7566;
salary      NUMBER(7,2);
dept_id     NUMBER(2):=59
dept_name   VARCHAR(14):='PERSONELL';
location    VARCHAR(13):='DALLAS';
emp_rec     emp%TYPE;
BEGIN
	EXECUTE IMMEDIATE 'CREATE TABLE bonus (id NUMBER, amt NUMBER)';
	sql_stmt:='INSERT INTO dept VALUES(:1,:2,:3)';
	EXECUTE IMMEDIATE sql_stmt USING dept_id, dept_name, location;
	sql_stmt:='SELECT * FROM emp WHERE empno=:id';
	EXECUTE IMMEDIATE sql_stmt INTO emp_rec USING emp_id;
	plsql_block:='BEGIN emp_pkg.raise_salary(:id,:amt); END;';
	EXECUTE IMMEDIATE plsql_block USING 7788, 500;
	sql_stmt:='UPDATE emp SET sal=2000 WHERE empno=:1 RETURNING sal INTO :2;';
	EXECUTE IMMEDIATE sql_stmt USING emp_id RETURNING INTO salary;
	EXECUTE IMMEDIATE 'DELETE FROM dept WHERE deptno=:num' USING dept_id;
	EXECUTE IMMEDIATE 'ALTER SESSION SET SQL_TRACE TRUE';
END;
```

# Cursore per SQL dinamico

---

Un cursore può anche non essere legato ad una query in particolare, potrebbe quindi essere aperto da qualsiasi query e potrà essere restituito come output di una funzione (tipo cursor)

```sql
comandoSQL:='SELECT * FROM studente WHERE ' || nomeAttributo || '=' || nomeValore;
OPEN nomeCursore FOR comandoSQL;
```

## Functions

<aside>
💡 Una funzione a differenza di una procedura restituisce un valore.

</aside>

---

## Struttura

---

```sql
CREATE [OR REPLACE] FUNCTION function_name
[parameter_name (IN | OUT | IN OUT] type [, ...])]
RETURN type
{IS | AS}
BEGIN
funct_body
END function_name;
```

## Esempio

---

```sql
CREATE FUNCTION circle_area(p_radius IN DOUBLE PRECISION) RETURNS DOUBLE PRECISION AS
$$
DECLARE
	v_pi DOUBLE PRECISION:=3.1415926;
	v_area DOUBLE PRECISION;
	BEGIN
		v_area:=v_pi*POWER(p_radius, 2);
		RETURN v_area;
	END
$$ LANGUAGE plpgsql;
```

# Call di una procedure e Call di una function

---

È possibile chiamare la procedura direttamente dalla console del DBMS

```sql
CALL <nome_procedura([lista_parametri])>;
```

Per quanto riguarda le funzioni è necessario chiamarla all’interno di una SELECT

```sql
SELECT <nomefunzione([lista parametri])>
FROM nome_tabella;
```

In PostgreSQL non c’è bisogno della clausola `FROM`, in Oracle si inserisce la clausola dual, che rappresenta una dummy table.

# Repository GitHub Esercizi

---

[https://github.com/simoneparente/BDD](https://github.com/simoneparente/BDD)