---
Date: September 23, 2022
Number: 3
Reviewed: Yes
Status: Done
author: Simone Parente Martone
---
# Architetture per i DBMS

## Architetture client-server

---

Si dividono in:

- Architetture a due livelli
    - Applicativi e interfacce ora si trovano sul lato client
    - Le funzionalità transazionali e di interrogazione rimangono al lato server
        - Java DataBase Connectivity (verrà ripresa nella parte finale del corso)
            - I client scritti in Java possono ora accedere a uno o più DBMS tramite un’interfaccia standard.
- A tre livelli
    - Aggiunge uno strato intermedio tra client e database server.
    - Esegue i programmi applicativi e memorizza le regole di business.
- A n livelli

### Sono server con specifiche funzionalità:

- File server
    - Mantiene e gestisce i file dei client
- Printer sever
    - È connesso a diverse stampanti
    - Le richieste di stampa sono inviate a questa macchina che le gestisce e processa
- Web server e email-server

## Modello Entity - Relationship


---

### Ciclo di vita dei sistemi informativi

---

1. Studio di fattibilità
    1. Si analizzano le aree di applicazione, i costi/benefici, si impostano le priorità tra le applicazioni.
2. Raccolta e analisi requisiti:
    1. Quali linguaggi, strutture, framework, ecc. usare
3. Progettazione dati.
4. Realizzazione.
5. Validazione e collaudo.
6. Funzionamento.
    1. Manutenzione

---

### Modelli concettuali

---

- Sono utilizzati nelle fasi preliminari di progettazione.
- Cercano di descrivere i concetti del mondo reale.
- Come correlare le tabelle (chiavi ecc.).
- Servono per ragionare sulla realtà di interesse.
- Si possono rappresentare le classi di dati di interesse.
- Prevedono efficaci rappresentazioni grafiche (utili anche per documentazione e comunicazione).

### Modello logico

---

- Utilizzati nei DBMS esistenti per l’organizzazione dei dati
    - utilizzati dai programmi
- indipendenti da strutture fisiche

---

### Progettazione Concettuale

> Deve escludere i dettagli di implementazione
> 

---

Individuare le informazioni rilevanti da memorizzare per soddisfare richieste informative e funzionali del caso applicativo. Interesse specifico per i dati:

Individuazione del problema degli aspetti informativi rilevanti:

- Entità [attributi, relazioni] (elementi informativi di base)
- Relazioni (modo in cui essi si relazionano)
- Vincoli (cosa un’entità può e non può fare)
- Interrogazioni della base dei dati (query)

- Il numero di utenti che possono interagire simultaneamente
- Frequenza con cui le interazioni avvengono

### Tipi di diagrammi

---

### Diagramma ER

---

Standard per la descrizione concettuale delle basi di dati (utilizzabile solo in questo campo)

- È definito proprio per la modellazione di basi di dati relazionali.
- I costrutti e le forme utilizzate sono adattate alla modellazione di un database.
- I dati sono descritti in 3 concetti fondamentali
    - entità
    - attributi
    - relazioni
    

### Class Diagram UML

---

Standard per la rappresentazione delle strutture dati nella programmazione a oggetti.

Classi = Associazioni

- I diagrammi UML sono utilizzati per molte attività di modellazione nel ciclo di vita di un software
- È anch’esso un linguaggio di modellazione unificato e può essere facilmente adattato.
- Cambia la rappresentazione diagrammatica ma non l’approccio alla progettazione.
- Offre una molteplicità di diagrammi
- L’insieme dei diagrammi (14) definisce il modello dell’applicazione.

## Esempio

---

- Una compagnia è organizzata in DIPARTIMENTI.
- Ogni dipartimento controlla dei PROGETTI [nome, numero, locazione].
- Per ogni IMPIEGATO si tiene traccia di [nome, SSN, indirizzo, ecc.].
- Ogni impiegato può lavorare su più PROGETTI ma appartiene a un solo DIPARTIMENTO.
- Teniamo traccia del numero ore settimanali che un impiegato spende su un determinato PROGETTO e del SUPERVISORE di ogni impiegato
- Ogni impiegato ha delle [PERSONE A CARICO], per ognuna delle quali registriamo [nome, sesso, data di nascita e parentela (con l’impiegato)]

## Entità

---

Corrispondono a classi di oggetti nel mondo reale che hanno proprietà omogenee, comuni ed esistenza autonoma nel mini-world

Può essere un oggetto fisico (casa, persona) o un oggetto concettuale (lavoro, società)

- In UML un’entità è detta classe

### Entità Debole

---

Una entità debole è una entità che non possiede chiavi candidate, di conseguenza viene collegata tramite una relazione 1:1 a un’altra entità forte, da cui otterremo la chiave (che chiameremo chiave esterna).

## Chiavi

---

Componenti principali dei diagrammi delle classi

- Corrispondono alle entità del modello ER.
- I dati vengono descritti insieme alle operazioni da svolgere su essi.

## Attributi

Ogni entità ha degli attributi

Esempio: l’impiegato ha nome, cognome, età, ecc

Ogni entità è caratterizzata da un set di valori per gli attributi

- ER
    
    Impiegato
    
    - nome
    - datanascita
    - indirizzo

- UML
    
    +Nome: String
    
    +DataNascita: Date
    
    +Indirizzo: Indirizzo (come tipo)
    
    Indirizzo:
    
    +Via: string
    
    +Città: string
    
- Possiamo distinguerli secondo diversi criteri
    - Divisibilità
        - Semplice (valore singolo)
        - Composto (divisibile in varie parti)
            - Esempio
                
                ```
                Persona (Nome, Cognome, DataN, { IndirizzoTelefono ({telefono (prefisso, numtelefono)}, Indirizzo(IndirizzoVia (Numero, Via, NumeroAppartamento),Città, Stato, CAP))})
                ```
                
    - Numero di valori
        - Single (età di un impiegato)
        - Multi (Attributo sede per entità Dipartimento)
            - In ER è rappresentato da un doppio cerchio
            - In UML può essere determinato un limite inferiore e superiore al numero di valori per un’entità
    - Calcolabile?
        - Archiviato (Data di nascita)
        - Derivabile (Età)

Valori nulli: non noto, non applicabile, magari esiste ma non è memorizzato (altezza di una persona).

## Intensione ed Estensione

---

Entità con stessi attributi di base sono raggruppati in un tipo di entità.

Intensione

Nome del tipo: Impiegato

Estensione

Insieme di Entità: Nome, Cognome, Età, Stipendio

Deve esistere per ogni entità una chiave o vincolo di unicità che deve avere un valore UNICO:

- Serve per identificare le singole entità
- Alcuni tipi di entità possono avere diversi attributi chiave (Se studente, avremo Matricola e Codice fiscale)
- Il vincolo di chiave deriva dai vincoli del mini-world
- Possono però esistere entità che non hanno attributi chiave
    - Quindi ci troviamo davanti a una entità debole.
Per identificare un attributo chiave:

- In ER sarà sottolineato o inserito come dot $\cdot$ pieno
- In UML:
    
    ```
    Matricola{id}: String
    Nome: String
    Cognome: String
    ```
    
    ## Se un attributo è chiave primaria non può essere derivato
    

### Dominio di un attributo

---

Ogni attributo è associato a un dominio che rappresenta l’insieme di valori assumibili dall’attributo

Età sarà compresa tra 16 e 70 e non oltre

Attributo - Entità - P(V) Insieme potenza dei sottoinsieme di V - V funzione

$$
A:E→P(V)
$$