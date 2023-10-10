---
author: Simone Parente
---
# Lezione 7

---

(d) in EER indica una scelta unica di una determinata sottoclasse

(o) indica una scelta multipla (non obbligatoria)

---

## Ristrutturazione del modello concettuale

---

Prima di passare allo schema logico è necessario ristrutturare il Class/ER Diagram in modo tale da:

- Semplificare la traduzione
- Ottimizzare il progetto

### Fasi

---

1. Analisi delle ridondanze.
2. Eliminazione delle generalizzazioni.
3. Eliminazione attributi multivalore.
4. Eliminazione attributi strutturati.
5. Partizionamento/Accorpamento di entità e associazioni.
6. Scelta degli identificatori principali.

### Tavole di analisi (Utili ma non indispensabili)

---

Indici di prestazioni (non valutabili esattamente in sede di programmazione logica)

- Costo di una operazione (numero di occorrenze di entità e relazioni visitate per rispondere a un’operazione).
- Per lo studio di questi dati dobbiamo conoscere:

- Volume dei dati
    - Numero di occorrenze di entità e relazioni
    - Dimensioni di ogni attributo

- Caratteristiche delle operazioni
    - tipo di operazione (interattiva o batch)
    - frequenza
    - dati coinvolti

---

### Tavola dei volumi

> concetto tipo volume
> 

---

Riportiamo tutti i concetti dello schema (entità e relazioni) con il volume previsto a regime

### Tavola delle operazioni

> operazioni tipo frequenza
> 

---

Riportiamo per ogni operazione la frequenza prevista e il tipo

### Tavola degli accessi

> concetto costrutto accessi tipo
> 

---

Riportiamo per ogni operazione il numero di accessi coinvolti e il tipo di accesso (L/S), tenendo a mente che le operazioni di scrittura sono più onerose di quelle in lettura

Il costo di un’operazione viene stimato contando il numero di accessi alle occorrenze entità e relazioni

### Esempi

- Tavola dei volumi
    
    
    
    Essa dipende da due parametri
    
    - Numero di occorrenze delle entità coinvolte nelle relazioni
    - Numero medio di partecipazioni di un’occorrenza di entità alle occorrenze di relazioni
    
- Tavola delle operazioni
    
    Operazioni:
    
    1. Assegna impiegato a progetto
    2. Trova dati di un impiegato, dipartimento in cui lavora e progetti a cui partecipa
    3. Trova i dati degli impiegati di un certo dipartimento
    4. Per ogni sede trova i dipartimenti con il cognome del direttore e l’elenco degli impiegati del dipartimento
    
    Per l’analisi andremo a valutare
    
    - Quali sono le operazioni che vengono fatte sulla base dei dati
    - Sulla base delle operazioni più frequenti andremo a vedere il costo per effettuarle
    
- Tavola degli accessi
    
    
    

# 1. Analisi delle ridondanze

---

<aside>
📌 Una **ridondanza** corrisponde alla presenza di un dato che può essere derivato da altri dati.

</aside>

### Vantaggi

---

- Semplificazione delle interrogazioni

### Svantaggi

---

- Appesantimento degli aggiornamenti
- Maggiore occupazione di spazio

### Come derivare un attributo

- Tramite altri attributi della stessa entità/associazione
    
    

- Tramite attributi di altre entità/associazioni
    

---

- Dal conteggio delle occorrenze


- Da associazioni in presenza di cicli
    - La presenza di cicli non genera necessariamente ridondanze
# 2. Eliminazione delle generalizzazioni

---

È necessario tradurre le generalizzazioni in altri costrutti

## Situazione Iniziale

---
## Tipi di generalizzazione

---

### a) Accorpare le figlie della generalizzazione nel padre

> Conveniente quando le operazioni non fanno troppa distinzione tra le occorrenze e tra gli attributi di $C_0, C_1, C_2$
> 

Le entità $C_1$ e $C_2$ vengono eliminate e le loro proprietà vengono aggiunte al padre $C_0$

### b) Accorpare il padre della generalizzazione nelle figlie

> Applicabile quando la generalizzazione è totale
(In caso contrario le occorrenze di $C_0$ che non sono occorrenze né di $C_1$ né $C_2$ non sarebbero rappresentate)
> 


### c) Sostituzione della generalizzazione con associazioni

> Applicabile quando la generalizzazione non è totale e ci sono operazioni che fanno distinzione tra entità padre ed entità figlie.
> 


Le entità $C_1$ e $C_2$  sono identificate esternamente all’entità $C_0$

- Vincoli
    
    ogni occorrenza di $C_0$ non può partecipare contemporaneamente a RG1 ed $R_{G2}$  se la generalizzazione è totale, ogni occorrenza di $E_0$ deve partecipare o ad un’occorrenza di $R_{G1}$  o ad un’occorrenza di $R_{G2}$
    

### Come scegliere tra le diverse alternative

---

> Per le generalizzazioni a più livelli si può procedere analizzando una generalizzazione alla volta a partire dal fondo della gerarchia
> 

La ristrutturazione delle generalizzazioni è un caso per cui il conteggio delle istanze e degli accessi non permette di scegliere sempre la migliore alternativa, anche ad occhio infatti, l’alternativa *c* sembra non convenire quasi mai perché richiede molti più accessi per eseguire le operazioni sui dati. Questa ristrutturazione però ha il vantaggio di generare entità con pochi attributi.

<aside>
💡 Avremo quindi delle strutture logiche di piccole dimensioni per cui un accesso fisico permette di recuperare molte tuple in una sola volta

</aside>

# 3. Eliminazione degli attributi multivalore

---


Il modello logico non consente una tale rappresentazione. Possiamo quindi:

1. Creare una entità esterna associata ad esso.
2. Trattare l’attributo come se fosse singolo
3. Replicare l’attributo nella classe

## 1) Creare un’entità esterna associata

---


## 2) Trattare l’attributo come se fosse singolo

---


## 3) Replicare l’attributo nella classe

---

- Per alcuni casi potrebbe andare bene e per un numero limitato di volte potrebbe essere una soluzione accettabile
    - Andare troppo oltre **potrebbe** causare un numero di campi vuoti eccessivo.

# 4. Eliminazione degli attributi strutturati

---

Per attributo strutturato si intende


## Soluzioni

---

### a) Introduzione di una classe per l’attributo strutturato

---

### b) Estrazione degli attributi della classe

---


### c) Trascurare la struttura dell’attributo


# 5. Partizionamento, accorpamento di entità/associazioni

---

## Accorpamento di entità

---

Per accorpamento di entità si intende un’unione dei concetti operando sulla struttura, è conveniente quando le operazioni accedono a dati presenti su entrambe le entità e si effettua su associazioni di tipo 1:1, è inoltre possibile la presenza di valori nulli.

### Esempio


Visto che le operazioni più frequenti su una persona richiedono sempre dei dati relativi all’appartamento che occupa possiamo fare così:

## Decomposizione di associazioni

---
# 6. Identificare chiavi primarie

<aside>
💡 Nel 99% dei casi ha senso inserire un ID alla classe (di tipo `SERIAL`), così da avere indici ridotti e maggior velocità di accesso a questi ultimi.

</aside>

---

Criteri da tenere a mente per la scelta delle chiavi primarie:

- Escludere attributi con valori nulli
- Minor numero di attributi (per avere dimensioni degli indici ridotte)
- Identificatore coinvolto in molte operazioni
- Velocità di accesso all’indice
    - minor tempo per confrontare i valori

Nel caso in cui nessuno degli identificatori candidati soddisfi tali criteri si introduce un ulteriore attributo all’entità, questo attributo conterrà dei codici generati appositamente per l’identificazione delle occorrenze.

- Esempio
    
    Nel caso in cui l’entità studente abbia due chiavi possibili
    
    - Matricola (10 caratteri, numerico)
    - Codice fiscale (16 caratteri, alfanumerico)
    
    È opportuno selezionare l’attributo matricola come identificatore primario perché richiede un tempo minore per confrontare due valori tra loro e quindi la velocità di accesso all’indice è ridotta