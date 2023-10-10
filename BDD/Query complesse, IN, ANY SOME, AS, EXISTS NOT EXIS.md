---
author: Simone Parente 
- Indice

# Query complesse

---

- Esempio
    
    > Fare una lista dei numeri di progetti per i progetti che
    coinvolgono un impiegato il cui cognome è ‘Smith’ come
    lavoratore oppure come manager del dipartimento che controlla il progetto
    > 
    - Esempio con query semplice
        
        ```sql
        (
        SELECT PNUMBER, LNAME
        FROM PROJECT,WORKS_ON,EMPLOYEE
        WHERE PNUMBER=PNO AND ESSN=SSN AND LNAME='Smith'
        )
        UNION
        (
        SELECT PNUMBER
        FROM PROJECT,DEPARTMENT,EMPLOYEE
        WHERE DNUM=DNUMBER AND MGR_SSN=SSN AND LNAME='Smith'
        )
        
        ```

        Risultato
        
    - Esempio con query annidata
        
        ```sql
        SELECT DISTINCT PNUMBER
        FROM PROJECT
        WHERE PNUMBER IN
        (
        SELECT PNUMBER
        FROM PROJECT,DEPARTMENT,EMPLOYEE
        WHERE DNUM=DNUMBER AND MGRSSN=SSN AND LNAME='Smith'
        )
        OR
        PNUMBER IN
        	(
        	SELECT PNO
        	FROM WORKS_ON,EMPLOYEE
        	WHERE ESSN=SSN AND LNAME='Smith'
        	);
        ```
        
# Operatore `IN`

---

L’operatore IN confronta un valore con un insieme di tuple union-compatibili e permette di specificare valori multipli nella clausola WHERE

- Esempio
    
    ```sql
    SELECT DISTINCT ESSN
    FROM WORKS_ON
    WHERE (PNO,HOURS) IN
    										(
    										SELECT PNO,HOURS
    										FROM WORKS_ON
    										WHERE ESSN='123456789'
    										);
    ```
    

# Operatore `ANY` (o `SOME`)

---

Operatore che confronta un singolo valore (attributo) v con un multiset V, restituendo TRUE se v è uguale a qualche **valore in V.

N.B. ANY e SOME sono equivalenti e possono essere combinati con $\{ >, \geq, <, \leq, <> \}$

$=ANY$ è equivalente a usare l’operatore $IN$

- Esempio
    
    ```sql
    SELECT FNAME,LNAME
    FROM EMPLOYEE
    WHERE SALARY>ANY(
    									SELECT SALARY
    									FROM EMPLOYEE
    									)
    ```
    

# Operatore `ALL`

---

Operatore che confronta un singolo valore (attributo) v con un multiset V, restituendo TRUE se v è uguale a tutti i valori in V.

Si può utilizzare con `SELECT`, `WHERE` e `HAVING` e può essere combinato con $\{ >, \geq, <, \leq, <> \}$

- Esempio
    
    > Trovare tutti i nomi degli impiegati il cui salario è maggiore del salario di tutti gli impiegati del dipartimento 5
    > 
    
    ```sql
    SELECT LNAME, FNAME
    FROM EMPLOYEE
    WHERE SALARY > ALL (SELECT SALARY
    											FROM EMPLOYEE
    											WHERE DNO=5);
    ```
    
# Keyword `AS`

---

È possibile rinominare ogni attributo che compare in una query tramite la keyword AS

- Esempio
    
    ```sql
    	SELECT E.LNAME AS EMPLOYEE_NAME,
    					S.LNAME AS SUPERVISOR_NAME
    	FROM EMPLOYEE AS E, EMPLOYEE AS S
    	WHERE E.SUPERSSN=S.SSN
    ```
# Ambiguità

---

Si parla di ambiguità nei casi in cui esistano attributi con lo stesso nome, uno in una relazione nella clausola `FROM` della query esterna e l’altro in una relazione di una clausola `FROM` della query interna

Per regola un riferimento a un attributo non qualificato fa riferimento alla relazione dichiarata nella query annidata più interna.

- Esempio 1
    
    > Trovare il nome di ogni impiegato che ha una persona a carico con lo stesso nome e lo stesso cognome dell’impiegato
    > 
    
    ```sql
    SELECT E.FNAME,E.LNAME
    FROM EMPLOYEE AS E
    WHERE E.SSN IN (
    									SELECT ESSN
    									FROM DEPENDENT
    									WHERE ESSN=E.SSN
    												AND DEPENDENT_NAME=E.FNAME
    												AND SEX=E.SEX)
    --In questo caso è necessario qualificare E.SEX altrimenti
    -- farebbe riferimento alla relazione DEPENDENT
    ```
    
    Risultato: Vuoto
    

In generale una query scritta con blocchi annidati è sempre possibile scriverla anche come un singolo blocco, infatti la query dell’Esempio 1 può essere scritta anche come

- Esempio 2
    
    ```sql
    SELECT E.FNAME,E.LNAME
    FROM EMPLOYEE AS E, DEPENDENT AS D
    WHERE E.SSN=D.ESSN AND E.SEX=D.SEX AND E.FNAME=D.DEPENDENT_NAME
    ```
    

# Operatore `CONTAINS` (eliminato)

---

Operatore che serviva per confrontare due insiemi, è stato poi eliminato per motivi di efficienza

- Esempio
    
    > Ritrovare il nome e il cognome di ciascun impiegato che lavora sum tutti i progetti controllati dal dipartimento 5
    > 
    
    ```sql
    SELECT FNAME, LNAME
    FROM EMPLOYEE AS E
    WHERE (
    				(
    				SELECT PNO
    				FROM WORKS_ON
    				WHERE E.SSN=ESSN
    				)
    				CONTAINS
    				(
    				SELECT PNUMBER
    				FROM PROJECT
    				WHERE DNUM=5
    			  )
    			)
    ```
    

# Operatori `EXISTS` e `NOT EXISTS`

---

Serve per verificare che una query annidata correlata sia vuota (o meno).

- Esempio
    
    > Trovare il nome degli impiegati che non hanno persone a carico
    > 
    
    ```sql
    SELECT FNAME,LNAME
    FROM EMPLOYEE
    WHERE NOT EXISTS
    						(
    							SELECT *
    							FROM DEPENDENT
    							WHERE SSN=ESSN
    						)
    ```

# Insiemi espliciti

---

- Esempio 1
    
    > Trovare SSN degli impiegati che lavorano su progetti 1, 2, 3
    > 
    
    ```sql
    SELECT DISTINCT ESSN
    FROM WORKS_ON
    WHERE PNO IN(1, 2, 3)
    ```
    

Si può testare anche se un valore è o meno **NULL:**

- $=$ e $\neq$ sono scritti come `IS` e `IS NOT` per confronti con NULL
- Esempio 2
    
    > Trovare il nome di tutti gli impiegati che non hanno supervisori
    > 
    
    ```sql
    SELECT FNAME,LNAME
    FROM EMPLOYEE
    WHERE SUPER_SSN IS NULL;
    ```
    
    

# Tabelle Joined

---

Possono essere usati i seguenti tipi di join

- **NATURAL JOIN**
- **INNER JOIN**
- **LEFT OUTER JOIN**
- **RIGHT OUTER JOIN**
- **FULL OUTER JOIN**
- Esempio
    
    > Trovare nome, cognome e indirizzo di ogni impiegato che lavora per il dipartimento “Research”
    > 
    
    ```sql
    SELECT FNAME,LNAME,ADDRESS
    FROM (EMPLOYEE JOIN DEPARTMENT ON DNO=DNUMBER)
    WHERE DNAME='Research'
    ```
    
    

## Aggregazione e raggruppamento

---

Le funzioni di aggregazione e raggruppamento incorporate in SQL sono:

- COUNT: conteggio tuple
    
    > Contare il numero di impiegati
    > 
    
    ```sql
    SELECT COUNT(*)
    FROM EMPLOYEE;
    ```
    
    > Contare il numero di tuple nel risultato della query
    > 
    
    ```sql
    SELECT COUNT(*) AS Conteggio
    FROM EMPLOYEE,DEPARTMENT
    WHERE DNO=DNUMBER AND DNAME='Research';
    ```
    
    > Elencare il nome ed il cognome degli impiegati con due o più persone a carico
    > 
    
    ```sql
    SELECT LNAME, FNAME
    FROM EMPLOYEE
    WHERE (SELECT COUNT(*)
    				FROM DEPENDENT
    				WHERE SSN=ESSN)>=2
    ```
    
- COUNT(DISTINCT): conteggio tuple distinte
    
    > Contare il numero di valori di stipendi distinti
    > 
    
    ```sql
    SELECT COUNT(DISTINCT SALARY)
    FROM EMPLOYEE;
    ```
    
- SUM: somma dei valori di un attributo in una tabella
- MAX: massimo valore tra attributi di una tabella
- MIN: minimo valore tra gli attributi di una tabella
- AVG: valore medio tra gli attributi di una tabella
- STD: deviazione standard tra gli attributi di una tabella (?)
- Esempio
    
    > Trovare la somma, il massimo, il minimo, e la media dei salari di tutti gli impiegati
    > 
    
    ```sql
    SELECT SUM(SALARY), MAX(SALARY), MIN(SALARY), AVG(SALARY)
    FROM EMPLOYEE
    ```
    

# Ordinamento di tuple (`ORDER BY`, `GROUP BY`)

---

## `ORDER BY`

---

Per ordinare le tuple nel risultato di una query si usa la clausola ********`ORDER BY`.**

- Esempio
    
    
    > Ritrovare una lista di impiegati e progetti su cui lavorano, ordinati per dipartimento e nell’ambito di ogni dipartimento, alfabeticamente per cognome e nome
    > 
    
    ```sql
    SELECT DNAME,FNAME,LNAME,PNAME
    FROM DEPARTMENT,EMPLOYEE,WORKS_ON,PROJECT
    WHERE DNUMBER=DNO AND SSN=ESSN AND PNO=PNUMBER
    ORDER BY DNAME,LNAME,FNAME;
    ```
    
    

L’ordinamento è di default crescente:

- ASC(ending): crescente
- DESC(ending): decrescente
- Esempio `ASC`/`DESC`
    
    > Per avere un ordine decrescente per dipartimento e crescente per nome e cognome
    > 
    
    ```sql
    ...
    ...
    ...
    ORDER BY DNAME DESC,LNAME ASC,FNAME ASC
    ```
    

## `GROUP BY`

---

Utilizzato per raggruppare tutte le tuple che hanno lo stesso valore per alcuni attributi

Le tuple sono divise in gruppi, ogni gruppo ha lo stesso valore per DNO

Le funzioni `COUNT` e `AVG` sono applicate a ciascun gruppo di queste tuple

- Esempio 1
    
    ```sql
    SELECT DNO, COUNT(*), AVG(SALARY)
    FROM EMPLOYEE
    GROUP BY DNO;
    ```
    
    
- Esempio 2
    
    > Per ogni progetto visualizzare il numero del progetto, il nome ed il numero di impiegati che lavorano su esso
    > 
    
    ```sql
    SELECT PNUMBER,PNAME,COUNT(*)
    FROM PROJECT,WORKS_ON
    WHERE PNUMBER=PNO
    GROUP BY PNUMBER,PNAME
    ```
    
    
- Esempio 3
    
    > Per ogni progetto visualizzare il numero del progetto, il nome e il numero di impiegati del dipartimento numero 5 che lavorano su di esso
    > 
    
    ```sql
    SELECT PNUMBER,PNAME,COUNT(*)
    FROM PROJECT,WORKS_ON,EMPLOYEE
    WHERE PNUMBER=PNO AND SSN=ESSN AND DNO=5
    GROUP BY PNUMBER,PNAME;
    ```
    
    

## Uso simultaneo di `HAVING` e `GROUP BY`

---

- Esempio 1
    
    > Per ogni progetto su cui lavorano più di due impiegati, visualizzare il numero del progetto, il nome del progetto e il numero di impiegati che lavorano su di esso
    > 
    
    ```sql
    SELECT PNUMBER,PNAME,COUNT(*)
    FROM PROJECT,WORKS_ON
    WHERE PNUMBER=PNO
    GROUP BY PNUMBER,PNAME
    HAVING COUNT(*)>2;
    ```
    
    
- Esempio 2
    
    > Determinare per ogni dipartimento che ha più di 3 impiegati, il numero totale di impiegati il cui stipendio è maggiore di 20k
    > 
    
    ```sql
    SELECT DNAME,COUNT(*)
    FROM DEPARTMENT, EMPLOYEE
    WHERE DNUMBER=DNO AND SALARY>20000
    GROUP BY DNAME
    HAVING COUNT(*)>3;
    ```
    

# Riepilogo interrogazioni

---

**SELECT** *<elenco attributi e funzioni>*

**FROM** *<elenco tabelle>*

| **WHERE** *<condizioni>* |

| **GROUP BY** *<attributo/attributi di raggruppamento>* |

| **HAVING** *<condizione di raggruppamento>* |

| **ORDER BY** *<elenco attributi>* |

|Facoltativi|

# Modifiche al database in SQL

---

Esistono tre comandi per modificare il database:

## `INSERT`

---

Il comando `INSERT INTO` inserisce nuove righe in una relazione. In caso non venissero specificati valori per tutti gli attributi, i non specificati assumeranno valore `DEFAULT` o `NULL`.

- Sintassi
    
    ```sql
    INSERT INTO Target[(Fieldname),...]
    VALUES(Value1,...);
    
    --oppure
    
    INSERT INTO Target[(Fieldname),...]
    SELECT FieldName,...
    FROM TableExpression;
    ```
    
- Esempio
    
    > Aggiungere una nuova tupla alla relazione Employee
    > 
    
    ```sql
    INSERT INTO EMPLOYEE
    VALUES (’Richard’, ‘K’, ‘Marini’, ‘654765876’, ’30-DEC-52’, ’98 Oak Forest, Katy, TX’, ‘M’, 37000, ‘987654321’, 4);
    ```
    

## `DELETE`

---

Il comando `DELETE` rimuove una o più tuple da una relazione

- Sintassi
    
    ```sql
    DELETE
    FROM TableName
    WHERE Criteria;
    ```
    
- Esempi
    
    > Elimina tutti gli impiegati che fanno di cognome ‘Brown’
    > 
    
    ```sql
    DELETE FROM EMPLOYEE
    WHERE LNAME='Brown';
    ```
    
    > Elimina tutti gli impiegati del dipartimento ‘Research’
    > 
    
    ```sql
    DELETE FROM EMPLOYEE
    WHERE DNO IN (SELECT DNUMBER
    								FROM DEPARTMENT
    								WHERE DNAME='Research'
    							 );
    ```
    

## `UPDATE`

---

Il comando `UPDATE` permette di modificare valori in una relazione

- Esempi
    
    > Modificare la location e il numero di dipartimento del progetto 10
    > 
    
    ```sql
    UPDATE PROJECT
    SET PLOCATION='Bellaire',DNUM=5
    WHERE PNUMBER=10;
    ```
    
    > Incrementare del 10% il valore dello stipendio degli impiegati del dipartimento ‘Research’
    > 
    
    ```sql
    
    UPDATE EMPLOYEE
    SET SALARY=SALARY*1.1
    WHERE DNO IN (SELECT DNUMBER
    								FROM DEPARTMENT
    								WHERE DNAME='Research'
    							 );
    ```
    

# AUTO_INCREMENT (non supportato)

Poteva essere usato per generare un identificatore unico per le nuove righe

- Esempio
    
    ```sql
    CREATE TABLE ANIMALS(
    id INT NOT NULL AUTO_INCREMENT
    name CHAR(30) NOT NULL,
    PRIMARY KEY(id)
    ) AUTO INCREMENT=5;
    
    INSERT INTO animals(name) VALUES
    ('dog'),('cat'),('whale'),('penguin'),('wolf'),('ostrich')
    ```
    
    Il risultato della query
    
    ```sql
    SELECT *
    FROM ANIMALS;
    ```
    
    Sarebbe:
    

# SERIAL

---

L’attributo SERIAL (ex AUTO_INCREMENT) può essere usato per generare un identificatore unico per le nuove righe:

È possibile resettare gli ID dati da un tipo serial col comando `ALTER SEQUENCE *tablename_serialcol*_seq RESTART WITH *new_current_id*;`

N.B: in caso di cancellazione di una tupla, l’id corrispondente a quest’ultima non sarà rimpiazzato da una successiva insert e in caso ci siano tuple successive, i loro id non verranno “scalati”.

- Esempio
    
    ```sql
    CREATE TABLE ANIMALS
    (
    id SERIAL
    name VARCHAR(30) NOT NULL,
    PRIMARY KEY(id)
    );
    ```
    

# Viste in SQL

---

Le viste sono tabelle derivate da tabelle esistenti nel database

Possono essere definite per nascondere dati presi da alcune tabelle (privacy), per combinare diverse tabelle insieme, creare report ecc.

- Sintassi
    
    ```sql
    CREATE VIEW ViewName
    AS SelectStatement;
    ```
    
- Esempi
    
    
    ```sql
    CREATE VIEW WORKS_ON1
    AS SELECT FNAME,LNAME,PNAME,HOURS
    FROM EMPLOYEE,PROJECT,WORK:ON
    ```
    
    
    ---
    
    ```sql
    CREATE VIEW DEPTS_INFO(
    							DEPT_NAME,NO_OF_EMPS,SAL
    												)
    						SELECT DNAME, COUNT(*), SUM(SALARY)
    						FROM DEPARTMENT,EMPLOYEE
    						WHERE DNUMBER=DNO
    						GROUP BY DNAME;
    ```