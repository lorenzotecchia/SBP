---
author: Lorenzo Tecchia
tags:
  - algorithm/sort
  - to-do/implementation
---
>[!todo] 
>- [ ] Implementazione in C

Insertion-Sort è un [[algoritmo]]  di [[ordinamento]] abbastanza efficiente per l'ordinamento di array di piccole dimensioni.
L'idea dell'algoritmo è quella di dividere la sequenza in una parte ordinata e una no.

All'inizio possiamo supporre che la sequenza ordinata sia composta solo dal primo elemento, ed il reato degli elementi contengono la sequenza disordinata.
Insertion-Sort prende il primo elemento della parte disordinata (nel nostro caso $j$) e lo inserisce nella giusta posizione nella parte disordinata.

Quindi se $a_{j-1} \leq a_{j}$ allora mantiene la stessa posizione. In caso contrario $a_{j-1}$ andrà in posizione $j$ e dovrà confrontare $a_{j}$ con $a_{j-2}$; anche in questo caso se $a_{j-2} \leq a_{j}$ andrà nella posizione precedentemente liberata ($j-1$), altrimenti è $a_{j-2}$ a spostarsi nella posizione $j-1$.

![[Pasted image 20231120160145.png|400]]

Ripetendo questo processo posso arrivare a confrontare $a_{j}$ con $a_1$:
- Se $a_{1}\leq a_j$ posizionerò $a_{j}$nella posizione $2$ (che sarà libera);
- In caso contrario andrà in posizione $1$ ed $a_{1}$ in posizione $2$ (questi spostamenti hanno ovviamente un costo loro).

![[Pasted image 20230826171202.png]]

A prescindere dalla condizione di terminazione del ciclo `while`(riga $6$), la riga $9$ è sempre la stessa infatti:
![[Pasted image 20231120160415.png]]

---
## Analisi
Studiamo solo il ciclo `while` in quanto unico a determinare il comportamento asintotico dell'algoritmo.

Questo ciclo può essere diverso per istanze con stessa dimensione a causa del confronto $\text{elem} \geq A|i|$ (questo è il motivo della preferenza del ciclo for)

Ne consegue che no possiamo associare un valore a $T(n)$ poiché non è detto che abbia lo stesso tempo di ogni istanza di $n$ elementi.

>[!example] 
> Per $(4,3,2,1)$ non verrà mai eseguito il corpo del ciclo, mentre per $(3,4,2,1)$ le istruzioni nel corpo saranno eseguire $6$ volte.

Questa irregolarità costringe a fare i seguenti ragionamenti:
- Se l'algoritmo è sfortunato possiamo dire che $T(n) = O(T_{max}(n))$ che rappresenta il tempo di esecuzione dell'algoritmo per i casi peggiori (quelli che fanno il massimo numero di operazioni)
- Se è molto fortunato, analogamente risulterà $T(n) = \Omega(T_{min}(n))$
- Se risulterà $T_{max}(n) = \Theta(T_{min}(n))$ è evidente che $T(n)$ avrà anch'esso lo stesso ordine, altrimenti dovrò analizzare il caso medio

Prima di analizzare in maniera esaustiva il ciclo `while`, vediamo la complessità delle altre linee. 
Per quanto riguarda il ciclo `while` bisogna innanzitutto, notare di come ci sono delle sequenze diverse che si comportano allo stesso modo; ovvero, tutte le sequenze che hanno la stessa relazione per ogni elemento in posizione $i-$esimo.$$(1, 3, 2, 4), (10, 25, 17, 60), (7, 29, 12, 30)\dots$$


---
### Correttezza
----
#### [[Analisi asintotica|Analisi]] dell'algoritmo iterativo
$$\sum^{n}_{i=1}T_{insert}(A,i) = \sum^{n}_{i=1}\Theta (k^{A}_{i}) = \Theta(\sum^{n}_{i=1}k^{A}_{i})$$
- Se $k^{A}_{i} = i$ (_caso peggiore_)
	$$\sum^{n}_{i=1}i = \frac{n(n+1)}{2} \rightarrow \Theta(n^{2})$$
	`Esempio: 10 9 8 7 6 5 4 3 2 1 0`

- Se $k^{A}_{i} = 1$ (_caso migliore_)
	$$\sum^{n}_{i=1}1 = n \rightarrow \Theta(n)$$
	`Esempio: 0 1 2 3 4 5 6 7 8 9 10`
#### [[Analisi asintotica|Analisi]] dell'algoritmo ricorsivo
![[appuntiIngenito.pdf#page=13]]

---
## Implementazione in C
```C
// da implementare
```