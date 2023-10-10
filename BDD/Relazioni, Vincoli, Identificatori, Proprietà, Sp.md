---
author: Simone Parente
---
# Lezione 4

---

## Relazioni/Vincoli ER

---

Le relazioni sono legami logici tra entità

Le istanze di relazione associano n entità dei tipi di relazione richieste

Ogni tipo di entità si dice partecipante al tipo di relazione

Impiegato→Lavora_per→Dipartimento

Impiegato
Tipo di entità

Lavora_Per
Relazione

Dipartimento
Tipo di entità

Il grado di un tipo di relazione è il numero di entità che vi partecipano.
Se il grado è 2, la relazione è detta binaria (che sono le più ricorrenti).

È possibile pensare ad una relazione come un attributo di una determinata entità.

Utilizzeremo quindi le relazioni per vincolare tra loro diverse entità, mantenendo gli attributi consistenti tra loro.
Ogni entità recita un ruolo per quella relazione, in alcuni casi un’entità partecipa più volte a una relazione, recitando ruoli diversi

### Relazione ricorsiva ER

---

Quando due entità dello stesso tipo hanno in comune una relazione.
Esempio: Persona $\iff$ è amico di $\iff$ Persona

### Vincoli ER

---

Le relazioni hanno dei vincoli che limitano le possibilità di combinare le entità nella formazione di relazioni, questi vincoli sono determinati dal mini-world che andiamo a rappresentare.

### Esempio

- Un impiegato può lavorare per **uno ed un solo** dipartimento
- Un dipartimento deve avere **almeno una** sede
- Un dipartimento deve avere **un solo** dirigente

- Vincoli di partecipazione

Specifica se l’esistenza di un’entità dipende dalla sua partecipazione a una relazione, permette quindi di specificare il numero minimo di istanze di relazione a cui le entità coinvolte possono partecipare

$\text{Impiegato} (1,1)$$\xrightarrow{lavora \;per}$$(0, n) Dipartimento$

- Impiegato: minimo 1 massimo 1 istanza
- Lavora per: minimo 0 massimo n istanze


- Vincolo di cardinalità

Indica il numero massimo di istanze di relazione a cui le occorrenze delle entità coinvolte possono partecipare

$\text{Impiegato} \xrightarrow{n} \text{Lavora per} \xrightarrow{1} \text{Dipartimento}$

Diversi impiegati possono lavorare per lo stesso dipartimento, ma un impiegato può lavorare soltanto per un dipartimento.


Nella maggior parte dei casi utilizziamo 3 valori per specificare le cardinalità: $0, 1,N$.

Il valore 0 per la cardinalità minima indica una partecipazione opzionale
Il valore 1 per la cardinalità minima indica una partecipazione obbligatoria
La cardinalità massima deve essere sempre specificata (altrimenti non conoscerei il tipo di relazione), la minima può essere omessa.

### Attributi di relazioni ER

---

Anche le relazioni possono avere degli attributi che le descrivono

### Entità deboli ER

---

Un’entità debole è un’entità che non possiede veri e propri attributi chiave, ha solitamente una chiave parziale ed è identificata tramite il collegamento con un entità di un altro tipo detta *entità identificante o proprietaria.* Un tipo di entità debole ha di solito una chiave parziale, se non esiste, nel peggiore dei casi avremo che tutti gli attributi dell’entità debole faranno parte della chiave parziale.

La relazione che correla l’entità debole all’entità forte è detta *relazione identificante.*

## Relazioni/Vincoli UML

---

In UML le relazioni sono dette **associazioni.**

Le associazioni binarie si rappresentano con semplici linee che congiungono le classi coinvolte, il nome della relazione è posto sulla linea (non è obbligatorio, possono esistere relazioni senza nome)

In caso ci sia un attributo della relazione (*classe di associazione*), l’associazione verrà descritta tramite una linea tratteggiata

> **Associazioni n-arie**: vengono rappresentate tramite un rombo collegato alle classi che partecipano all’associazione
> 

### Identificatori UML

---

Non esiste una notazione per esprimere identificatori di classi

Si possono definire vincoli di integrità su associazioni e attributi specificandoli tra parentesi graffe (vincolo utente)

Es. {id}
In caso diversi attributi presentino la dicitura {id}, l’attributo identificatore sarà composto

Le molteplicità di default è 1 (e possono essere omesse)

La cardinalità “molti” viene rappresentata dal simbolo * (0..*) *(indica 0 a N)*

Per gli identificatori esterni si usa uno stereotipo

- Si usano per estendere i costrutti base UML quando si vuole modellare un concetto non modellabile tramite i costrutti di base
- Vengono indicati da un nome incluso tra parentesi angolari <<  >>

### Proprietà delle associazioni UML

---

Con una freccia è possibile indicare un **verso privilegiato di navigabilità** **di un’associazione.
Si possono specificare aggregazioni di concetti.

- Il rombo bianco indica che un oggetto della classe parte **può esistere** senza dover appartenere a una classe aggregante


un tecnico può non avere un team

- Il rombo nero indica che un oggetto della classe parte **non può** esistere senza appartenere a un oggetto della classe aggregante


un posto non può esistere senza una sala in cui è posizionato

È possibile inserire note/commenti come documentazione

## Modello EER (Enchanced ER)

---

Il modello EER offre costrutti per ampliare i concetti di base di ER:

- **Sottoclassi** e **superclassi**
- **Specializzazioni** e **Generalizzazioni**
- **Categorie**
- ecc.

Servono per modellare un miniworld in maniera più accurata

### Sottoclassi, Superclassi ed ereditarietà

---

Un entità può avere ulteriori estensioni per massimizzare la sua significatività

### Esempio

Un impiegato può essere categorizzato in

- Segretario
- Ingegnere
- Tecnico

- Manager (si/no)

- Stipendiato
- Pagato_a_ore

- Ognuna delle entità che appartiene a un sottoinsieme della classe impiegato è detta sottoclasse, Impiegato è superclasse per ognuna di queste entità.
- Ogni istanza di ognuna delle entità membro di una sottoclasse rappresenta la stessa istanza dell’entità SUPERCLASSE, non può esistere un’istanza di una SOTTOCLASSE che non sia anche nell’istanza della SUPERCLASSE
- Ogni istanza membro di una sottoclasse eredita tutti gli attributi e tutte le relazioni della sua superclasse

## Specializzazione

---

Il processo di specializzazione permette di definire un insieme di sottoclassi per una determinata classe

### Vincolo di disgiunzione

---

Un’istanza può essere membro al più di una sottoclasse

## Generalizzazione

---

- La **generalizzazione** rappresenta il processo inverso alla **specializzazione**

### Vincolo di completezza

---

Se è **TOTALE** specifica che ogni istanza della **superclasse** deve appartenere a una delle **sottoclassi**

Se è **PARZIALE** specifica che possono esserci istanze delle **superclassi** che non appartengono ad alcuna **sottoclasse** nella specializzazione

Indicata con una linea singola in EER.

Avremo quindi 4 tipi di specializzazione/generalizzazione 

1. Disgiunta, totale
2. Disgiunta, parziale
3. Overlapping, totale
4. Overlapping, parziale

Per Overlapping si intende che quando le classi non sono disgiunte (un’istanza può essere membro di diverse sottoclassi).

### Generalizzazioni e Specializzazioni in ER

---

Eventuali proprietà possono essere rappresentate tramite {e}