---
Date: 2001-01-01
Number: 11
Reviewed: Yes
Status: Done
author: Simone Parente Martone
---
# Algebra relazionale
---
In che ordine le operazioni devono essere fatte per recuperare determinate informazioni da uno schema relazionale?
# Selezione e Proiezione
Selezione: Decomposizione orizzontale
- Filtraggio delle tuple
Proiezione: Decomposizione verticale
## Operatore SELECT
$_{\boldsymbol{si \; indica \; con \; \sigma}}$
WHERE in SQL
---

Usato per selezionare sottoinsiemi di tuple in una relazione che soddisfa una condizione di selezione

- È un operatore unario
- È commutativo

Sintassi:

- $\sigma_{selection\_condition}(<relazione>)$
- Esempio
    
    $\sigma_{dno=4}$(Employee) restituisce il sottoinsieme degli impiegati che lavora nel dipartimento numero 4
    
    $\sigma_{salary>3000}$(Employee) restituisce il sottoinsieme degli impiegati con salario >3000$
    
- Nell’SQL la SELECT tipicamente specificata nella clausola WHERE

La condizione di selezione è un’espressione booleana formata da clausole dalla forme:

$$
<nome\_attributo> \bold{op\_confronto} <valore \; costante>
$$

$$
<nome\_attributo> \bold{op\_confronto} <nome\_attributo>
$$

Eventualmente concatenate con operatori di confronto:

- Esempio
    
    $\sigma_{(dno=4 \; and \; Salary>25000 \; \textcolor{red}{OR} \; dno=5 \; and \; Salary>30000)}$(Employee)
    
- Operatori di confronto
    
    $=, \neq, <, >, \leq, \geq$
    

## Operatore PROJECT $\pi$
SELECT in SQL

---

Usato per selezionare un sottoinsieme delle colonne di una relazione

- Non è commutativa

Sintassi:

- $\pi_{<attribute\_list>}(<relazione>)$

La relazione risultante avrà gli attributi specificati in $attribute\_list$.

La PROJECT rimuove automaticamente potenziali tuple duplicate nel caso in cui non ci sia una chiave candidata.

Le tuple risultanti saranno sempre minori o uguali del numero di tuple di partenza della tabella.

## Operatore RENAME

---

- È un operatore unario

Per rinominare correttamente gli attributi in una relazione che risulta dall’algebra relazionale, listiamo i nuovi nomi di attributi in parametri:

$$
TEMP=⁍(EMPLOYEE)
$$

$$
R(FirstName,LastName,Salary)=\pi_{<FNAME,LNAME,SALARY>}(TEMP)
$$

# Operazioni Insiemistiche
Essedo una relazione un insieme di tuple, nel caso in cui queste ultime fossero ***union compatibili*** è possibile applicarvi le classiche operazioni insiemistiche.

Il risultato nella combinazione di due relazioni è una nuova relazione.
## Union compatibility
Due relazioni $R(A_1, A_2, \ldots, A_n)$ e $S(B_1,B_2,\ldots,B_n)$ sono union compatibili se hanno lo stesso grado e se

$$
dom(A_i)=dom(B_i) \; \; \; \; per \; 1 \leq i \leq n
$$

## Operazioni union compatibili
Nel caso in cui due relazioni R ed S siano ***************************************************union compatibili*************************************************** è possibile effettuare le operazioni di:
# Unione $\cup$
> Commutativa, Associativa, applicabile a qualsiasi numero di relazioni.

Il risultato di $R \; \cup \; S$ è la relazione che include **tutte** le tuple che sono in R, **tutte** le tuple che sono in S e **tutte** le tuple che sono presenti in entrambe, eliminando i duplicati.

- Esempio di unione
    Trovare il SSN di tutti gli impiegati che lavorano o nel dipartimento n° 5 o supervisionano direttamente un impiegato che lavora nel dipartimento n° 5.
    - $DEPS\_EMPS=$$\sigma_{dno=5}$
    - $Result1$=$\pi_{SSN}(DEPS\_EMPS)$
    - $Result2=\pi_{SUPERSSN}(DEPS\_EMPS)$
    - $RESULT=Result1 \; \cup \; Result2$
    
    ![esempio union.png](esempio_union.png)
# Intersezione $\cap$
> Commutativa, Associativa, applicabile a qualsiasi numero di relazioni

Il risultato dell’operazione $R \; \cap \; S$ è la relazione che include solo le tuple che sono **sia in $R$ che in $S$**
# Differenza $-$
Il risultato dell’operazione $R-S$ è la relazione che include tutte le tuple che **sono presenti in R ma non in S**.

Il risultato dell’operazione $S-R$ include tutte le tuple che sono **presenti in S ma non in R**.

È un’operazione non commutativa

# Esempi di operazioni $\cup \; \cap \; -$

![Relazione S](relazione_studente.png)

Relazione S

![Relazione I](relazione_instructor.png)

Relazione I

---

### $S \cup I$

![S cup I.png](S_cup_I.png)

### $S \cap I$

![S cap I.png](S_cap_I.png)

### $S-I$

![S - I.png](S_-_I.png)

### $I-S$

![I - S.png](I_-_S.png)

---
# Prodotto cartesiano (Cross Join) $\times$

Il prodotto cartesiano è un’operazione binaria che darà come risultato un numero di n-uple pari al prodotto delle cardinalità degli operandi.

Le relazioni non è necessario che siano **union compatibili** (dato che le n-ple sono tutte combinabili)

- $R(A_1, A_2, \ldots, A_n) \times S(B_1, B_2, \ldots, B_n) =Q(A_1, A_2, \ldots, A_n, B_1, B_2,\ldots, B_n)$
- In Q si ha una tupla per ogni combinazione di una da R ed una da S
- Se R contiene $n_r$ tuple ed S contiene $n_r$ allora $R \times S$ contiene $n_r \cdot n_s$ tuple.

Nel caso ci fossero attributi con lo stesso nome nelle due relazioni si deve effettuare il rename di uno dei due.

- Esempio 1
    
    Dato lo schema relazionale AZIENDA, vogliamo trovare per ogni impiegato di sesso femminile, una lista dei suoi familiari a carico
    
    - $FEMALE\_EMPS=\sigma_{Sex="F"}(EMPLOYEE)$
    - $EMPNAMES=\pi_{<FNAME,LNAME,SSN>}(FEMALE\_EMPS)$
    - $EMP\_DEPENDENTS=EMPNAMES \times DEPENDENTS$
    - $ACTUAL\_DEPENDENTS=\sigma_{SSN=ESSN}(EMP\_DEPENDENTS)$
    - $RESULT=\pi_{<FNAME,LNAME,DEPENDENT\_NAME>}(ACTUAL\_DEPENDENTS)$
    
    Otterremo quindi la tabella
    
    ![esempio prodcart.png](esempio_prodcart.png)
    
- Esempio 2
    
    ![esempio prodcart2.png](esempio_prodcart2.png)
    

# JOIN $\Join$

$\sigma_{join-condition}$ $(R \times S)$ è piuttosto frequente come operazione e quindi è chiamata JOIN

Denotata con $\Join$ è usata per combinare diverse tuple in una sola.

$\sigma_{join-condition}(R \times S)$  diventa $R \Join_{join-condition}S$

- Esempio
    - Supponiamo di voler trovare il nome del manager di ciascun dipartimento
        - Dobbiamo combinare ogni tupla dipartimento con la tupla impiegato il cui SSN fa match con il valore MGRSSN nella tupla dipartimento
    
    $$
    DEPT\_MGR=DEPARTMENT\Join_{MGRSSN=SSN}EMPLOYEE
    $$
    $$
    RESULT=\pi_{DNAME,LNAME,FNAME}(DEPT\_MGR)
    $$
    ![join esempio.png](join_esempio.png)
- Esempio su prodotto cartesiano
    L’Esempio 2 sul prodotto cartesiano, di operazioni:
    
    $EMP\_DEPENDENTS=EMPNAMES \times DEPENDENTS$
    
    $ACTUAL\_DEPENDENTS=\sigma_{SSN=ESSN}(EMP\_DEPENDENTS)$
    
    Può essere ridotto a un’operazione
    
    $$
    ACTUAL\_DEPENDENTS=EMPNAMES\Join_{SSN=ESSN}DEPENDENTS
    $$
    

# Funzioni aggregate e di raggruppamento

$_{Non \; presenti \; nell'Algebra \;Relazionale  \; base}$

---

Operano su insiemi di dati per restituire come risultato una relazione con un unico valore.

Sintassi:

$\textcolor{pink}{_{<attributi \; di \; raggruppamento>}} \digamma\textcolor{orange}{_{<lista \; funzioni>}}\textcolor{red}{(R)}$

- Dove <attributi di raggruppamento> indica una lista di attributi della relazione R e raggruppa le tuple presenti nella relazione sulla base dei loro valori
- <lista funzioni> è una lista di coppie <funzione> <attributo>
    - <funzione> è una delle funzioni SUM, AVERAGE, MAX, MIN, COUNT…
        - Approfondite in 
    - <attributo> è un attributo della relazione R