---
author: Simone Parente
---
# Fasi della progettazione di un database

---

1. Specifica e **analisi dei prerequisiti**
2. Progettazione **Concettuale**
3. Progettazione **Logica**
4. Progettazione **Fisica**

## Data Model

<aside>
💡 Un modello deve:
- Rappresentare una certa realtà
- Fornire un insieme di simboli per rappresentare questa realtà

</aside>

---

- Introducono una forte astrazione dei dati, nascondendo i dettagli agli utenti.
- L’astrazione di questi dati consiste in:
    - Una struttura delle basi di dati
        - tipi di dati, vincoli che specificano relazioni e/o restrizioni che intercorrono tra essi
    - Le operazioni per manipolare le strutture
        - `INSERT`, `DELETE`, `SELECT`, `UPDATE`, ecc.

- Un comportamento dinamico per permettere all’utente di definire operazioni sui dati
    - Ad esempio una operazione `CALC_MEDIA_VOTO` che calcola la media dei voti e può essere applicata a un oggetto studente.

### Modello concettuale

<aside>
💡 Fornisce dei simbolismi per rappresentare oggetti astratti in modo indipendente.

</aside>

### Modello logico

<aside>
💡 Traduce le strutture concettuali in strutture logiche gestite da un DBMS.

</aside>

---

## Categorie di data model

---

1. Ad alto livello
2. A basso livello
3. Rappresentazionali
4. Autodescrittivi

1. Object/Entity based
    1. Per esempio il [modello E-R](https://it.wikipedia.org/wiki/Modello_E-R)
    2. Utilizzano:
        1. Entità
        2. Attributi
        3. Relazioni
2. Fisici, hanno anche dettagli su come sono memorizzati i dati nel calcolatore
3. I più utilizzati di questa categoria sono di tipo:
    1. Relazionale
    2. Reticolare
    3. Gerarchico

Questi ultimi sono modelli di dati record-based.

## Schemi basi di dati

---

### Schema o Metadati

Descrive la struttura logica della base di dati (ma non il contenuto)

Lo schema del database è specificato in fase di progetto, non dovrebbe quindi cambiare (troppo spesso) in futuro.

### Istanza

Descrive il contenuto del database in un particolare istante di tempo
Ogni volta che il database viene modificato si crea una nuova istanza.

# Il corso si baserà su PostgreSQL

Nonostante questo alcuni esempi saranno in Oracle e saranno presi dalle slide (non mi prendo responsabilità sulla correttezza di questi ultimi). La stragrande maggioranza degli esempi in PostgreSQL li ho testati personalmente e dovrebbero essere giusti.

---

# Architettura a 3 livelli

---

1. External level
2. Conceptual level
3. Internal level
	- Mapping
1. Descrive strutture e vincoli
	    nome
	    cognome
	    annoNascita
3. Descrive le strutture di storing fisiche
# Indipendenza dei dati

## Indipendenza logica

- È possibile modificare lo schema concettuale senza cambiare necessariamente applicativo o gli schemi esterni

## Indipendenza fisica

- Lo schema interno può essere cambiato senza dover cambiare gli schemi
concettuali (o esterni)
- Più facile da ottenere

## Vantaggi

- Abbiamo la possibilità di ottenere una reale indipendenza dei dati molto facilmente.
- Il database risulta essere più flessibile e scalabile.

## Svantaggi

- Il catalogo del DBMS dovrà avere dimensioni maggiori.
- I due livelli di mapping creano un overhead durante la compilazione o esecuzione di una query di un programma, causando inefficienze nel DBMS.