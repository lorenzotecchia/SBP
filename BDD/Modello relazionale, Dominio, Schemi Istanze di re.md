---
Date: September 29, 2022
Number: 5
Reviewed: Yes
Status: Done
author: Simone Parente Martone
---
# Schema logico

## **Modello** relazionale


È il modello più diffuso data la sua semplicità e i formalismi matematici su cui poggia. Si basa sul concetto di relazione**,** le relazioni vengono rappresentate tramite tabelle, il database è rappresentato come una collezione di tabelle.

## Dominio

Insieme di valori indivisibili

- Esempio
    
    **Social_Sec_Number**: insieme di SSN validi, di 9 cifre
    
    **Names**: Insieme di nomi di persone
    
    **Employee_ages**: possibile età dei dipendenti, 16→80
    
    **Academic_Dep**: insieme di dipartimenti universitari
    

Per ogni dominio viene specificato un **tipo di dato**, potrebbe essere necessario (o utile) specificare un’unità di misura

### Relazione

- A ogni dominio è associato un nome che descrive il ruolo del dominio
- L’ordinamento tra gli attributi è irrilevante (struttura non posizionale)
- Ogni riga del modello è detta tupla

### Schemi di relazione

Uno schema di relazione descrive una relazione ed è formato da:

- Un nome (Dipartimento)
- Una lista di attributi (DName, DNumber, MGRSSN, MGRStartDate)

Ciascun attributo è il nome di un ruolo di un dominio all’interno dello schema

Il grado di una relazione è il numero di attributi del suo schema di relazione

- Esempio
    
    Relazione Student
    
    Grado 7 (nome, ssn, cell, addr, phone, age, gpa)
    
    $Dom(Name)=Names$ (Il dominio di “Name” sono tutti i nomi)
    
    $Dom(SSN)=\text{Social Security Number}$
    

### Istanza di relazione

Una relazione r dello schema R, denotata r(R) è un insieme di tuple di r.

Uno schema di database relazionale è un insieme di schemi di relazione. $S_0\{ R_1,R_2,\ldots,R_m \}$.

Un’istanza di database relazionale DB è un insieme di istanze di relazione $DB=\{r_1,r_2,\ldots,r_m\}$.

### Vincoli del modello relazionale

Nel modello relazionale i valori presenti in un’istanza devono soddisfare una serie di vincoli

1. Dominio
2. Vincolo di chiave
3. Vincolo di integrità di entità
4. Vincolo di integrità referenziale

1. Il valore di ciascun attributo di A deve essere un valore atomico (`char`, `int`, `string` a lunghezza fissa o variabile, `data`, `ora` ecc.)
2. Una relazione è un insieme di tuple distinte, devono esistere dei sottoinsiemi di attributi con la proprietà di non avere la stessa combinazione di valori in più tuple, sia **superkey** un tale sottoinsieme $t_1[\red{sk}]\neq t_2[\red{sk}]$
L’insieme di questi attributi è detto superkey
Una superkey minimale è una chiave che ha il minimo numero di attributi tale da rendere la chiave una superkey.
    - Esempio
        
        In una relazione possono esistere diverse chiavi, dette chiavi candidate, ne scegliamo solo una che sarà la chiave primaria.
        Una chiave deve avere delle proprietà di invarianza nel tempo (l’età sicuramente non andrà bene)
        
        Una superkey può essere una serie di attributi che presi insieme rendono unico una tupla
        Nome, Cognome, Data di nascita oppure semplicemente un SSN
        
        Nel caso sia presente un SSN, la chiave minimale sarebbe SSN.
        
3. Nessun valore di chiave primaria può essere `null`
4. Questo vincolo è specificato tra due relazioni e sono usati per mantenere consistenti le tuple delle due relazioni,  un insieme di attributi FK in uno schema di relazione $R_i$ è una chiave esterna se vale che: a. gli attributi in FK hanno stesso dominio degli attr. della chiave in $R_i$.