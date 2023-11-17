---
author: Lorenzo Tecchia
tags:
  - definition
---
Una ***ricorrenza*** è una equazione o disequazione che descrive una funzione in termini dei suoi valori su input più piccoli.

>[!tip] 
> Per risolvere al pieno equazioni di ricorrenza ricorre in ogni caso, utilizzare un mix dei metodi proposti qui sotto.

>[!important]
> Permette di descrivere i [[Analisi asintotica#Notazione $ Theta$|tempi di esecuzione]] degli algoritmi divide et impera.

>[!note] Albero di ricorrenza
> Un albero dove i nodi rappresentano le chiamate ricorsive e ad ogni nodo è associato il numero di ricorrenza e il contributo locale di tale nodo(abbiamo in questo modo anche il contributo di ogni livello dell'albero)

>[!example] # Esempio fattoriale
> Prendiamo come esempio la funzione del fattoriale
> $$n= \begin{cases}1 & \text { se } n=1 \\ n \cdot(n-1) ! & \text { altrimenti }\end{cases}$$
> Che sarà in termini di equazioni di ricorrenza:$$T_F(n)= \begin{cases}\Theta(1) & \text { se } n=1 \\ T_F(n-1)+\Theta(1) & \text { altrimenti }\end{cases}$$
> C'è una corrispondenza tra il livello dell'albero e l'output del programma. Avremmo infatti al livello $i$ un output $n -1$. 
> La foglia invece, per essere definita tale deve ricevere l'input del caso base (si noti infatti che il $\Theta(1)$ della foglia non è lo stesso $\Theta(1)$ degli altri livelli).
> Il livello foglia se $n- i = 1 \Longrightarrow i = n -1$
> A questo punto possiamo calcolare, partendo dal livello $0$ il tempo di esecuzione della funzione fattoriale:$$T_F(n)=\sum_{i=0}^{n-1} \Theta(1)+\Theta(1)=\Theta(n)$$
> ![[Pasted image 20231117144545.png|200]]

>[!important]
> Per comprendere il numero di chiamate ricorsive che la suddetta funzione compie bisogna analizzare la struttura utilizzando l'albero di ricorrenza
## Forma generale di equazioni di ricorrenza con funzioni a un solo parametro
Forniamo una generalizzazione della struttura dell'equazione di ricorrenza:$$
T(n)=\left\{\begin{array}{l}
\Theta(1) \text { se } n \leq k \\
z(n) \\
\sum_{i=0}^{z(n} T\left(f_i(n)\right)+g(n) \text { se } n>k
\end{array}\right.$$
- Il caso base, in linea di massima, è una costante $\rightarrow$ Potrebbero presentarsi casi in cui il caso base abbia un numero di operazioni lineare e quindi invece di avere un $\Theta(1)$ avremo un $\Theta(n)$
- $g(n)$ è il contributo delle operazioni nelle chiamate ricorsive
- $z(n)$ è il numero di chiamate
> [!note] alcune note su $z(n)$
> $z(n)$ viene definita come una funzione e non come una costante in quanto il numero di chiamate potrebbero dipendere dal valore in input $\rightarrow$ Non è detto che una chiamata debba fare lo stesso numero di chiamate ricorsive di un'altra chiamate nello stesso algoritmo

- $f_{i}(n)$ è l'input che prende ogni chiamata ricorsiva (non è detto che sia la stessa per ogni chiamante), ed ovviamente, affinché risulti corretto l'algoritmo deve risultare $f_{i}(n) < n$
È importante notare che per calcolare il numero di nodi di un livello basta moltiplicare tra loro le espressione dei livelli precedenti, ad esempio:
![[Pasted image 20231117145247.png]]
>[!example] # Primo esempio sulle equazioni di ricorrenza
> Sia $z(n) = 2$ (si hanno $2$ chiamate ricorsive per ogni chiamata $\rightarrow$ questo si traduce in un albero binario) e siano:
> - $f_{i}(n) = \frac{n}{4}$(suddivisione input)
> - $g(n) = n^{2}$(tempo di esecuzione della altre istruzioni)
> Avremo la seguente equazione asintotica:$$T(n)= \begin{cases}1 & \text { se } n \leq 1 \\ 2 T\left(\frac{n}{4}\right)+n^2 & \text { se } n>1\end{cases}$$
> Che viene rappresentata dal seguente albero di ricorrenza:
> ![[Pasted image 20231117153222.png]]
> Dall'albero di ricorrenza capiamo che il termine generale di un input al livello i-esimo è $\frac{n}{4^{i}}$(termine che ci permette di calcolare l'altezza dell'albero)
> Si noti che vale la seguente proprietà: $$f_i(n)=f_j(n), \forall 1 \leq i, j \leq z(n)$$
> Quindi ogni nodo di ciascun livello ha lo stesso input $\rightarrow$
> - A livello $0$ avremo contributo $g(n) = n^{2}$
> - A livello $1$ avremo contribuito $g\left(\frac{n}{4}\right)= (\frac{n}{4})^2$
> - A livello $2$ avremo contributo $g\left(\frac{n}{4^{2}}\right)= \left(\frac{n}{4}\right)^{2}$
> - E così via
> È conveniente mantenere i risultati il più generale possibile(senza semplificare) in modo da non perdere le relazioni tra i livelli e poterne ricavare più semplicemente la somma
> Per il calcolo totale possiamo isolare i livelli (quindi calcolare il contributo di ongi livello) e in seguito effettuare un'unica somma in verticale(è necessario conoscere l'altezza dell'albero). 
Dunque:

 |   Livello   | Contributo                                  |
 |-----------| ------------------------------------------- |
 | Livello $0$ | $n^{2}$                                     |
 | Livello $1$ | $2 \cdot \left(\frac{n}{4}\right)^{2}$      |
 | Livello $2$ | $2 \cdot 2\left(\frac{n}{4^{2}}\right)^{2}$ |
 | Livello $3$ | $2^{3}\left(\frac{n}{4^{3}}\right)^{3}$     |
 |   $\dots$   | $\dots$                                     |

 >[!example] # Primo esempio sulle equazioni di ricorrenza
 > Per quanto riguarda l'altezza dell'albero bisogna ragionare sul  contributo delle foglie, che sappiamo essere $1 \rightarrow$ Tale contributo può essere relazionato alla dimensione dell'input di un livello $i$ (nel nostro caso $\frac{n}{4^{i}}$). Per calcolare l'altezza dell'albero:$$\begin{align}
\frac{n}{4^i}=1 \Longrightarrow n=4^i \Longrightarrow \log _4 n=i \log _4 4 \stackrel{\log _a}{\Longrightarrow} \stackrel{x=\frac{\log _n x}{\log _n a}}{\Longrightarrow} \frac{\log _2 n}{\log _2 4}=i \Longrightarrow \frac{\log n}{2 \log 2}=i\\ \Longrightarrow i=\frac{\log n}{2}\end{align}$$
 > Visto che l'altezza dell'albero è $h = \frac{1}{2}\log(n)$, il numero delle foglie sarà il numero dei figli elevato all'altezza dell'albero. 
 > Nel nostro caso:$$\begin{align}
T(n)=\text { contributo c.b. }\cdot  n_f+\sum_{i=0}^{h-1}\left(\begin{array}{c}
\text { termine } \\
\text { generale }
\end{array}\right)=\sqrt{n}+\sum_{i=0}^{\frac{\log n}{2}-1}\left(\frac{n^2}{8^i}\right) \Longrightarrow \\ \sqrt{n}+n^2 \sum_{i=0}^{\frac{\log n}{2}-1}\left(\frac{1}{8^i}\right)^i\end{align}$$
> Ma essendo $0 < \frac{1}{8}< 1$ si tratta di una serie geometrica convergente $\rightarrow$ Questo ci semplifica lo studio della sommatoria grazie al seguente ragionamento:$$
\underbrace{\sum_{i=0}^0 x^i}_{x^0=1} \leq \sum_{i=0}^z x^1 \leq \underbrace{\sum_{i=0}^{\infty} x^i}_{\frac{1}{1-x}} \Longrightarrow 1 \leq \underbrace{\sum_{i=0}^z x^i}_{\text {tende ad una costante }} \leq \frac{1}{1-x}$$
> Visto che la nostra serie tende ad una costante $k$ avremo che:$$
T(n)=\sqrt{n}+k n^2=k n^2+n^{\frac{1}{2}}=\Theta\left(n^2\right)$$
> Volendo utilizzare la forma chiusa invece delle proprietà di converga avremo che:$$\begin{align}
\sum_{i=0}^{\frac{\log n}{2}-1}\left(\frac{1}{8}\right)^i=\frac{\left(\frac{1}{8}\right)^{\frac{\log n}{2}}-1}{\frac{1}{8}-1}=\frac{-\left(\frac{1}{8}\right)^{\frac{\log n}{2}}}{-\frac{1}{8}+1}=\frac{1-\left(\frac{1}{8}\right)^{\frac{\log n}{2}}}{\frac{7}{8}}=\frac{8}{7}\left(1-\left(\frac{1}{8}\right)^{\frac{\log n}{2}}\right)=\frac{8}{7} \\ \left(1-\left(\frac{1^3}{2^3}\right)^{\frac{\log n}{2}}\right)= \frac{8}{7}\left(1-\left(\left(\frac{1}{2}\right)^{\log n}\right)^{\frac{3}{2}}\right)=\frac{8}{7}\left(1-\frac{1}{\left(2^{\log n}\right)^{\frac{3}{2}}}\right)=\frac{8}{7}\left(1-\frac{1}{\sqrt{n^3}}\right)\end{align}$$
>
> La funzione $f(n) = 1 - \frac{1}{1\sqrt{n^{3}}}$ tenderà a $1$ per $n \rightarrow \infty$; pertanto $\frac{8}{7}$ sarà il limite superiore della nostra sommatoria.
> Per $n = 1$ risulta $f(1) = 0$, ma allora la nostra sommatoria tenderà ad una costante $c$ tale che $0 \leq c \leq \frac{8}{7}$ dunque:$$
T(n)=\sqrt{n}+c n^2 \Theta\left(n^2\right)$$

## Risoluzioni
### Sostituzione
Nel ***metodo di sostituzione***, ipotizziamo un limite e poi usiamo l'induzione matematica per dimostrare che la nostra ipotesi sia corretta
#### Esempio
### Albero delle ricorrenze
Il ***metodo dell'albero delle ricorrenze o albero di [[ricorsione]]*** converte la ricorrenza in un albero i cui nodi rappresentano i costi ai vari livelli della ricorsione; per risolvere la ricorrenza, adotteremo delle tecniche che limitano le sommatorie.
>[!tip] 
> Di solito, in questo caso, è buona norma andare a disegnare l'albero delle ricorrenze fino ad un livello che ci permetta di interpretare l'andamento

Quando si risolve un'equazione di ricorrenza con albero delle ricorrenza, vanno tenute a mente le seguenti informazioni:
1. Numero del livello
2. Input
3. Contributo ad ogni livello
4. Numero di rami
5. Totale
Ad ogni passo quindi:
- Sostituiamo l'input 
- Verifichiamo il contributo dei nodi
- Calcoliamo il numero di rami ad ogni chiamata ricorsiva
- Calcoliamo il totale moltiplicando il contributo dei nodi per il numero di rami
#### Esempio
| Livello | Input             | Contributo        | Rami                                                   | Totale                                   |
| ------- | ----------------- | ----------------- | ------------------------------------------------------ | ---------------------------------------- |
| 0       | $n$               | $n$               | 1                                                      | n                                        |
| 1       | $n^{\frac{1}{3}}$ | $n^{\frac{1}{3}}$ | $n^{\frac{2}{3}}$                                      | $n^{\frac{1}{3}}\cdot n^{\frac{2}{3}}=n$ |
| 2       | $n^{\frac{1}{9}}$ | $n^{\frac{1}{3}}$ | $n^{\frac{2}{3}}\cdot n^{\frac{2}{9}}=n^{\frac{8}{9}}$ |$n^{\frac{1}{9}}\cdot n^{\frac{8}{9}}=n$                                          |
### Metodo dell'esperto
Il ***metodo dell'esperto*** fornisce i limiti per ricorrenze nella forma $$T(n)=a\;T(n/b)+f(n)$$
dove $a\geq 1, b > 1$ e $f(n)$ è una funzione data.
#### Esempio