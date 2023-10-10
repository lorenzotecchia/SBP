---
author: Simone Parente
---
- Indice

# Lezione 12

---

Le foreign key non vanno inserite nel modello concettuale

---

# Query base SQL

---

In SQL si possono avere diverse tuple identiche in tutti gli attributi, quindi una tabella SQL non è un insieme di tuple, è bensì un multiset di tuple. Alcune relazioni possono essere vincolate ad essere insiemi utilizzando un vincolo di chiave oppure la clausola `DISTINCT` mentre si usa lo statement `SELECT`.

# Interrogazione: *SELECT*
Modifica: *`INSERT`, `DELETE`, `UPDATE`*

---

## SELECT

---

- Istruzione base per recuperare informazioni da un database
- Non ha relazioni con l’operatore SELECT in algebra relazionale
- Le istruzioni SELECT con una sola relazione nella clausola FROM ci permettono di realizzare
    - selezioni, proiezioni e ridenominazioni
- Le istruzioni SELECT con più relazioni nella clausola FROM ci permettono di realizzare JOIN e Prodotti Cartesiani
- Notazione
    
    ```sql
    SELECT <lista_attributi>
    FROM <lista_tabelle>
    WHERE <condizione>
    ```
    
    Dove:
    
    - ************************************<lista_attributi>** è una lista di nomi di attributi i cui valori devono essere recuperati dalla query.
    - ****************************<lista_tabelle>** è una lista di nomi di relazioni da cui ricavare le tuple.
    - **************************<condizione>** è un’espressione booleana di ricerca che identifica la tupla da ritrovare.
- Esempi
    
    > Trovare la data di nascita e l’indirizzo dell’impiegato “John B. Smith”
    > 
    
    ```sql
    SELECT BDATE,ADDRESS
    FROM EMPLOYEE
    WHERE FNAME='John',MINIT='B',LNAME='Smith';
    ```
    
    In algebra relazionale sarebbe:
    
    $$
    \pi_{BDATE, ADDRESS}(\sigma_{FNAME='JOHN' \; AND \; MINIT='B' \; AND \; LNAME='SMITH'}(EMPLOYEE)
    $$
    
    ---
    
    > Trovare il cognome, nome e indirizzo degli impiegati del dipartimento “Research”.
    > 
    
    ```sql
    SELECT Cognome, Nome, Indirizzo,
    FROM EMPLOYEE, DEPARTMENT,
    WHERE Dnome='Research' AND DNUMBER=DNO;
    ```
    
    In algebra relazionale sarebbe:
    
    $$
    \pi_{FNAME,LNAME,ADDRESS}(\sigma_{DNAME='Research'}(EMPLOYEE\Join_{DNO=DNUMBER}DEPARTMENT))
    $$
    

# RENAMING, DISTINCT e Operazioni Insiemistiche

---

In SQL è possibile utilizzare lo stesso nome per diversi attributi se questi ultimi appartengono a relazioni diverse.

Se una query coinvolge tali relazioni occorre qualificare il nome dell’attributo con il nome della relazione per evitare ambiguità. 
**`Employee.SSN`,* in questa scrittura *********Employee********* è detto alias.
È inoltre possibile rinominare gli attributi della relazione all’interno della query in questo modo

```sql
--La query seguente è ricorsiva
FROM EMPLOYEE AS E(FN,MI,LN,SSN,BD,ADDR,SEX,SAL,SSSN,DNO)
```

## Mancanza della clausola WHERE

---

In delle query in cui non è presente la clausola WHERE avremo che:

- La clausola sottintesa sarà `WHERE TRUE` cioè **tutte le tuple** della relazione specificata nella clausola FROM faranno parte del risultato
    - Nel caso in cui più di una relazione è specificata nella clausola FROM otterremo come risultato il prodotto cartesiano delle relazioni
- Esempi
    
    > Selezionare tutti i SSN
    > 
    
    ```sql
    SELECT SSN
    FROM EMPLOYEE;
    ```
    
    ---
    
    > Selezionare tutte le combinazioni Employee.SSN e Department.Dname
    > 
    
    ```sql
    SELECT SSN, DNAME
    FROM EMPLOYEE, DEPARTMENT;
    ```
    

## Il carattere JOLLY `*`

---

Per recuperare **tutti** gli attributi delle tuple selezionate si utilizza il carattere JOLLY `*`.

- Esempi
    
    > Trovare tutti i valori degli attributi degli impiegati che lavorano per il dipartimento n° 5
    > 
    
    ```sql
    SELECT *
    FROM EMPLOYEE
    WHERE DNO=5;
    ```
    
    > Trovare tutti gli attributi di Employee e gli attributi di Department per cui lavora ogni impiegato del dipartimento ‘Research’
    > 
    
    ```sql
    SELECT *
    FROM EMPLOYEE,DEPARTMENT
    WHERE DNAME='Research' AND DNO=DNUMBER
    ```
    

## Duplicazioni di tuple in SQL

---

SQL non tratta relazioni come insiemi quindi delle tuple duplicate possono apparire più di una volta e non vengono eliminate per i seguenti motivi:

- All’utente potrebbero interessare le duplicazioni
- È un’operazione costosa (l’implementazione richiederebbe prima l’ordinamento delle tuple e poi l’eliminazione delle stesse)

## Clausola DISTINCT

---

Se non si è interessati a ottenere duplicati, possiamo specificarlo con la clausola DISTINCT

- Esempi
    
    > Trovare i salari di tutti gli impiegati
    > 
    
    ```sql
    SELECT SALARY
    FROM EMPLOYEE
    ```
    
    > Trovare i salari degli impiegati (se esistono due salari con stesso valore, questo valore apparirà una sola volta nella query seguente)
    > 
    
    ```sql
    SELECT DISTRINCT SALARY
    FROM EMPLOYEE
    ```
    

## Operazioni Insiemistiche

---

SQL incorpora le seguenti operazioni insiemistiche (**devono essere union compatibili**):

- `UNION`
- `EXCEPT`
    
    Restituisce tutti i valori distinti della query a sinistra dell’operando - che non sono presenti nella query a destra.
    **N.B.** Questa operazione cancellerà le tuple duplicate a meno che non venga richiesto il contrario tramite la clausola ALL. 
    
- `INTERSECT`
- Esempi
    
    > Fare una lista dei numeri dei progetti per i progetti che coinvolgono un impiegato il cui cognome è ****‘Smith’**** come lavoratore **oppure** come manager del dipartimento che controlla il progetto
    > 
    
    ```sql
    (
    SELECT PNUMBER
    FROM PROJECT,WORKS_ON,EMPLOYEE
    WHERE PNUMBER=PNO AND ESSN=SSN AND LNAME='Smith'
    )
    UNION
    (
    SELECT PNUMBER
    FROM PROJECT,DEPARTMENT,EMPLOYEE
    WHERE DNUM=NUMBER AND MGRSSN=SSN AND LNAME='Smith'
    )
    ```
    

# Confronto tra sottostringhe

---

Per confrontare tra loro diverse stringhe si usa l’operatore **LIKE**.

Caratteri jolly:

- *%*, rimpiazza qualsiasi numero di caratteri
- *_* rimpiazza un singolo carattere
- Esempi
    
    > Trovare tutti gli impiegati il cui indirizzo è a ‘Houston, Texas’
    > 
    
    ```sql
    SELECT FNAME,LNAME
    FROM EMPLOYEE
    WHERE ADDRESS LIKE '%HOUSTON,TEXAS%';
    ```
    
    > Trovare le persone che hanno un nome che inizia per ‘A’ e ha una ‘d’ come terza lettera:
    > 
    
    ```sql
    SELECT *
    FROM PERSONE
    WHERE NOME LIKE 'A_d%';
    ```
    
    > Mostrare i salari risultanti se a tutti gli impiegati che lavorano sul progetto ‘Product X’ venisse concesso un aumento del 10%
    > 
    
    ```sql
    SELECT FNAME, LNAME, 1.1*SALARY
    FROM EMPLOYEE, WORKS_ON, PROJECT
    WHERE ESSN=SSN AND PNO=PNUMBER AND PNAME='Product X';
    ```