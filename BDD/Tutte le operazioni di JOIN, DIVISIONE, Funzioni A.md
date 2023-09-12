---
Date: October 20, 2022
Number: 14
Reviewed: Yes
Status: Done
author: Simone Parente Martone
---
# Operazioni di Join
## Theta Join
---
Una join con $\theta$ generica è detta THETA JOIN.

Il join più comune ha come $\theta$ l’operatore di uguaglianza ed è detto EQUIJOIN (nei risultati dell’equi-join abbiamo sempre una coppia di valori di attributi identici).

- Esempio
    
    ![Esempio theta join.png](Esempio_theta_join.png)
    

## Natural Join

---

> La NATURAL JOIN è un tipo di operazione che ci permette di correlare due o più tabelle sulla base di valori uguali in attributi contenenti lo stesso tipo di dati.
> 

L’operazione NATURAL JOIN, denotata da **,* è praticamente una EQUIJOIN che elimina l’attributo duplicato.

I due attributi di join (per ogni coppia) devono avere lo stesso nome, in caso contrario bisogna prima fare un’operazione di renaming.

### Sintassi AR

$$
\green{Q}=\blue{R}^*(\blue{<list_1>})(\red{<list2>})\red{S}
$$

Dove

- $\blue{<list_1>}$ è la lista di attributi presi da R
    - È quella che verrà mantenuta nel risultato
- $\red{<list_2>}$ è la lista di attributi presi da S
- R ed S sono due relazioni

Se nessuna combinazione di tuple soddisfa la condizione di join, la relazione risultate avrà zero tuple.

- Tabelle
    
    Date due tabelle PERSONA e AUTO
    
    ### PERSONA
    
    | NOME | NUM_PATENTE |
    | --- | --- |
    | Antonio | 123 |
    | Giovanni | 156 |
    | Arturo | 172 |
    
    ### AUTO
    
    | TARGA | NUM_PATENTE |
    | --- | --- |
    | VT AC73949 | 156 |
    | ROMA J1003 | 172 |
    | MI GH3434 | 300 |
    | NA G666223 | 301 |
- Esempio Algebra Relazionale
    
    $R=\green{PERSONA} \Join \blue{AUTO}$
    L’attributo NUM_PATENTE è detto attributo di join.
    
- Esempio SQL
    
    Per ottenere una natural join delle tuple delle due tabelle avremo bisogno di una query così strutturata
    
    ```sql
    SELECT *
    FROM PERSONA
    NATURAL JOIN AUTO;
    ```
    
    Così da ottenere come risultato:
    
    | Num_Patente | Nome | Targa |
    | --- | --- | --- |
    | 156 | Giovanni | VT AC73949 |
    | 172 | Arturo | ROMA J1003 |

## Join Esterno

---

Il join esterno estende, assegnandovi valori nulli, tutte le tuple che verrebbero tagliate fuori da un join interno.

- Sinistro (⟕ oppure $\Join_{LEFT}$)
    
    Mantiene tutte le tuple del primo operando (estendendole)
    
    ![esempio leftjoin.png](esempio_leftjoin.png)
    

- Destro   (⟖ oppure $\Join_{RIGHT}$)
    
    Mantiene tutte le tuple del secondo operando (estendendole)
    
    ![esempio rightjoin.png](esempio_rightjoin.png)
    

- Completo (⟗ ****oppure $\Join_{FULL}$)
    
    Mantiene tutte le tuple di entrambi gli operandi (estendendole)
    
    ![esempio fulljoin.png](esempio_fulljoin.png)
    

# Divisione

---

L’operazione divisione è indicata con $\div$ ed è un particolare tipo di interrogazione che talvolta si presenta nelle applicazioni di basi di dati.

Per esempio: date delle tabelle *****Voli***** e *****Linee*****

### ****Voli****

---

| CODICE | DATA |
| --- | --- |
| AZ427 | 21/07/2001 |
| AZ427 | 23/07/2001 |
| AZ427 | 24/07/2001 |
| TW056 | 21/07/2001 |
| TW056 | 24/07/2001 |
| TW056 | 25/07/2001 |

### *Linee*

---

| CODICE |
| --- |
| AZ427 |
| TW056 |

L’operazione $Voli \div Linee$ 

darà come risultato:

| DATA |
| --- |
| 21/07/2001 |
| 24/07/2001 |

Mentre l’operazione $(Voli \div Linee)\Join Linee$

darà come risultato:

| CODICE | DATA |
| --- | --- |
| AZ427 | 21/07/2001 |
| AZ427 | 24/07/2001 |
| TW056 | 21/07/2001 |
| TW056 | 24/07/2001 |

## Insieme completo di operazioni
---
È possibile provare che l’insieme $\{\sigma, \pi, \cup, -, \times \}$  è un insieme completo, cioè che tutte le altre operazioni possono essere espresse tramite combinazioni di queste ultime.
## Esempi
### Intersezione
---
$R \cap S=(R\cup S)-((R-S)\cup(S-R))$
### Join
---
$R\Join_{<condition>}S=\sigma_{<condition>}(R\times S)$
### Divisione
---
$R \div S = T1 \xleftarrow{} \pi_{<attribute \, of \, R-attribute \, of \, S>}(R)$
$T2 \xleftarrow{} \pi_{<attribute \, of \, R-attribute \, of \, S>}((S \times T1)-R)$
$T \xleftarrow{}T1-T2$
---
# Limiti dell’Algebra Relazionale
---
- Non è possibile derivare valori, quindi non possiamo ottenere:
    - **conversioni, somme, differenze**
    - **somme, medie, mediane, etc.**
---
# Funzioni aggregate e di raggruppamento
$_{Non \; presenti \; nell'AR \; base}$
---
Operano su insiemi di dati per restituire come risultato una relazione con un unico valore.

- Sintassi
    
    $\pink{_{<attributi \; di \; raggruppamento>}} \digamma\orange{_{<lista \; funzioni>}}\red{(R)}$
    
    - Dove <attributi di raggruppamento> indica una lista di attributi della relazione R e raggruppa le tuple presenti nella relazione sulla base dei loro valori
    - <lista funzioni> è una lista di coppie <funzione> <attributo>
        - <funzione> è una delle funzioni SUM, AVERAGE, MAX, MIN, COUNT…
            - Approfondite in 
        - <attributo> è un attributo della relazione R