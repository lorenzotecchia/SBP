---
author: Simone Parente Martone
---
# Lezione 8

---

### Indice

# Traduzione verso un modello logico

---

## Restrizioni dell’ER Ristrutturato

---

1. Non ci sono generalizzazioni/specializzazioni
2. Non ci sono attributi multipli all’interno delle entità
3. Non ci sono attributi strutturati all’interno delle entità

---

## Algoritmo di traduzione da ER a relazionale

---

1. Mappatura di tipi di entità
2. Traduzione di tipi di entità deboli
3. Mappatura di tipi di relazioni binarie 1:1
4. Mappatura di tipi di relazioni binarie 1:N
5. Mappatura di tipi di relazioni binarie M:N 
6. Traduzione di attributi multivalore
7. Mappatura di tipi di relazioni n-arie
8. Opzioni per la mappatura della specializzazione o della generalizzazione
9. Traduzione dei tipi unione (categorie)

---

## 1. Mappatura di tipi di entità

---

Per ogni tipo di *entità forte E* si costruisca una *relazione R* che contenga tutti gli attributi semplici di *E*. Nel caso di attributi composti si inseriscano solo gli attributi componenti semplici.

La chiave primaria di *R* sarà uno degli attributi chiave di *E*, se la chiave è composta, l’insieme di attributi semplici che la compongono sarà la chiave primaria di *R*

Le relazioni create dalla mappatura di tipi di entità sono chiamate relazioni entità, ogni tupla rappresenta un’istanza di un’entità.

## 2. Traduzione di tipi di entità deboli

$_{Esempio \;pagina \;292}$

---

Per ogni *entità debole W* con tipo di entità proprietaria E si costruisca una relazione R e si inseriscano tutti gli attributi semplici (o componenti semplici di attributi composti) di W come attributi di R. Si inseriscano come attributi di chiave esterna di R tutti gli attributi di chiave primaria delle relazioni corrispondenti ai tipi di entità proprietari. La chiave primaria di R sarà data dalla combinazione di:

- Chiavi primarie delle entità proprietarie
- Chiave parziale del tipo di entità debole W (se esiste)

Nel caso ci trovassimo davanti a un’entità debole $E_2$ il cui proprietario è un’altra entità debole $E_1$, $E_1$ dovrà essere mappato prima di $E_2$ in modo da determinare prima la chiave primaria di $E_1$

## 3. Mappatura di tipi di relazioni binarie 1:1

$_{Esempio \; pagina \; 293}$

---

Per ogni *relazione R binaria 1:1* nello schema ER si individuino le relazioni S e T corrispondenti ai tipi di entità che partecipano a *R*.

Approcci possibili:

1. Basato su chiavi esterne (da utilizzare sempre se non ci sono particolari motivi per non farlo)
2. Basato sulla fusione delle relazioni
3. Basato su riferimenti incrociati o relazioni di relazioni

### 1. Approccio basato su chiavi esterne

Iniziamo scegliendo una delle relazioni (in questo caso S), si inserisca in S come chiave esterna la chiave primaria di T.

S sarà un tipo di entità con partecipazione totale a R, i suoi attributi saranno tutti gli attributi semplici (o componenti semplici di attributi composti) del tipo di associazione 1:1 indicata con R.

<aside>
⚠️ È possibile includere la chiave primaria di S come chiave esterna di T (sconveniente nella maggior parte dei casi)

</aside>

### 2. Approccio basato sulla relazione con fusione

È possibile fondere i due tipi di entità e la relazione in una sola relazione.

<aside>
⚠️ Questo approccio ha senso solo quando entrambe le partecipazioni sono totali, poiché ciò indica che le due tabelle avranno sempre lo stesso numero di tuple

</aside>

### 3. Approccio basato su riferimenti incrociati o relazione di relazioni

Creare una terza relazione R con lo scopo di definire un riferimento incrociato tra le chiavi primarie e le due relazioni S e T che rappresentano i due tipi di entità (questo approccio è necessario per le relazioni binarie M:N.

La relazione R sarà una relazione di relazioni perché ogni tupla di R è un’istanza di relazione che collega una tupla di S con una tupla di T.
Gli attributi delle chiavi primarie di S e T saranno incluse nella relazione R come chiavi esterne. La chiave primaria di R sarà una delle due chiavi esterne, l’altra chiave esterna sarà una chiave univoca di R

<aside>
⚠️ È necessaria un’operazione di join aggiuntiva quando si combinano le tuple collegate alle due tabelle (visto che abbiamo una relazione in più)

</aside>

## 4. Mappatura di tipi di relazioni binarie 1:N

---

Approcci possibili:

1. Basato su chiave esterna
2. Basato su riferimenti incrociati o relazioni di relazioni

### 1. Approccio basato su chiavi esterne

Per ogni relazione R binaria 1:N:

- Si individui la relazione S che rappresenta il tipo di entità partecipante al lato-N del tipo di relazione
- Si inserisca in S come chiave esterna la chiave primaria della relazione T (l’altro tipo di entità partecipante a R)
- Si inseriscano fra gli attributi di S tutti gli attributi semplici (o componenti semplici di attributi composti) del tipo di relazione 1:N

### 2. Approccio basato sulla relazione di relazioni

Creiamo una relazione separata R i cui attributi sono le chiavi primarie di S e T (che saranno anche chiavi esterne verso S e T).
La chiave primaria di R corrisponderà alla chiave primaria di S.

<aside>
⚠️ Questa operazione può essere utilizzata se un numero limitato di tuple in S partecipa alla relazione, così da evitare un numero elevato di valori nulli nella chiave esterna

</aside>

## 5. Mappatura di tipi di relazioni binarie M:N

---

<aside>
⚠️ In questo caso non è possibile rappresentare un tipo di associazione M:N tramite attributi di chiave esterna in una delle due relazioni partecipanti, dato il rapporto di cardinalità M:N, occorre quindi creare una nuova relazione S distinta

</aside>

Data una relazione R binaria M:N, andremo a creare una nuova relazione S che rappresenti R e inseriremo come attributi di chiave esterna di S le chiavi primarie delle relazioni che rappresentano i tipi di entità partecipanti, la combinazione tra questi due formerà la chiave primaria di *S.*

## 6. Traduzione di attributi multivalore

---

Per ogni attributo multivalore A costruiremo una nuova relazione R che comprenderà un attributo corrispondente ad A più l’attributo di chiave primaria K (che sarà chiave esterna di R) della relazione che rappresenta il tipo di entità o il tipo di relazione che ha A come attributo.
La chiave primaria di R è data dalla combinazione di A e K, in caso di attributi composti considereremo le sue componenti semplici.

I tipi di associazione n-ari (n>2) vengono mappati in modo simile ai tipi di relazione M:N inserendo il passo 7. nell’algoritmo di mappatura

## 7. Mappatura di tipi di relazioni n-arie

---

Per ogni tipo di relazione n-aria (n>2) R costruiremo una nuova relazione S per rappresentare R.

In S inseriremo le chiavi primarie delle relazioni che rappresentano i tipi di entità partecipanti come attributi di chiave esterna. Inseriremo anche come attributi di S tutti gli attributi semplici del tipo di relazione n-aria .

La chiave primaria di S è solitamente una combinazione di tutte le chiavi esterne che fanno riferimento alle relazioni che rappresentano i tipi di entità che vi partecipano.

## 8. Opzioni per la mappatura di specializzazioni o generalizzazioni

---

- Notazione
    - Attr(R) indica gli attributi della relazione R
    - PK(R) indica la primary key di R

Data una specializzazione con m sottoclassi

$$
\{ S_1, S_2,\ldots S_m\}
$$

E superclasse C, i cui attributi sono

$$
\{k, a_1, \ldots, a_n\}
$$

con PK(C)=k, possiamo utilizzare le seguenti opzioni per mapparla secondo il modello logico

### Opzione 8A: relazioni multiple - superclasse e sottoclasse

---

<aside>
💡 Questa opzione è utilizzabile con qualsiasi tipo di specializzazione.(totale o parziale, disgiunta o sovrapposta)

</aside>

Costruiremo una relazione L per C con attributi $Attr(L)=$$\{k, a_1,\ldots, a_n \}$ e $PK(L)=k$, realizzeremo una relazione $L_i$ per ogni sottoclasse $S_i$, con $1 \leq i \leq m$ avente come attributi:

$$
Attr(L_i)=\{k\} \cup \{Attr(S_i)\} ; \; PK(L_i)=k
$$

### Opzione 8B: solo relazioni di sottoclasse

---

<aside>
💡 Questa opzione è utilizzabile solo per una specializzazione le cui sottoclassi sono totali

</aside>

Specializzazione totale: ogni entità nella superclasse appartiene a almeno una delle sottoclassi

<aside>
💡 È raccomandata solo se la specializzazione ha vincolo di disgiunzione

</aside>

Costruiremo una relazione $L_i \; \forall \;$sottoclasse $S_i, \; 1 \leq i \leq m$ con  

$$
Attr(L_i)=\{ \, attributi \;di \; s_i \} \cup \{k, a_1, \ldots, a_n\};\; PK(L_i)=k
$$

### Opzione 8C: singola relazione con un attributo tipo

---

<aside>
💡 Adatta a specializzazioni in cui le sottoclassi sono disgiunte, può produrre molti attributi NULL se nelle sottoclassi ci sono molti attributi specifici

</aside>

Costruiremo una singola relazione L con attributi:

$$
Attr(L_i)=\{k, a_1, \ldots, a_n\}\;\cup \; Attr(S_1) \; \cup \ldots\; \cup \; Attr(S_m) \; \cup \; \{t\} ; \; PK(L_i)=k
$$

dove t è un attributo **********tipo********** o **************************discriminante************************** e indica la sottoclasse a cui appartiene ciascuna tupla

### Opzione 8D: singola relazione con molti attributi tipo

---

Costruiremo un singolo schema di relazione L con attributi:

$$
Attr(L)=\{k, a_1, \, \ldots,\, a_n \} \;\cup \; Attr(S_1) \; \cup \ldots\; \cup \; Attr(S_m) \; \cup \; \{t_1, \ldots t_m\} ; \;
$$

$$
PK(L)=k
$$

Dove ogni tipo $t_i$ con $1\leq i \leq m$ è un attributo di tipo ********bool******** che indica se la tupla appartiene a una sottoclasse $S_i$

---

Le opzioni 8A e 8B sono opzioni di relazioni multiple

Le opzioni 8C e 8D sono opzioni di relazioni singole

## 9.Traduzione dei tipi unione (categorie)

$_{Esempio \; pagina \; 302}$

---

Per mappare una categoria le cui superclassi di definizione hanno chiavi diverse, di norma si specifica un nuovo attributo chiave, detto ********************************chiave surrogata********************************. Questo perché le chiavi delle classi che la definiscono sono diverse, non è quindi possibile utilizzare nessuna di loro per identificare tutte le entità della categoria.

A ogni relazione corrispondente verrà quindi aggiunta la chiave surrogata, che avrà valore NULL nei casi in cui l’entità non fosse membro della relazione corrispondente.