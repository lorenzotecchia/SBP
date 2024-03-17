## 2023-03-17
 Si scriva un algoritmo ricorsivo che, presi in ingresso un albero binario $T$ contenente dati interi e un intero positivo $k$, restituisca il valore della massima profondità dei nodi con valore di chiave multiplo di $k$. Nel caso l'insieme di tali nodi fosse vuoto, è richiesta la restituzione del valore di default $-1$. L'algoritmo dovrà essere efficiente e non far uso né di variabili globali né di parametri passati per riferimento. Infine, si scriva un algoritmo iterativo che simuli precisamente l'algoritmo ricorsivo di cui sopra.

## 2022-10-19

Si scriva un algoritmo ricorsivo che, dati in ingresso un albero binario di ricerca $T$ e un intero positivo $k$, cancelli da $T$ tutti i nodi che si trovano in posizioni multiple di $k$ nell'ordinamento totale delle chiavi dell'albero. Tale algoritmo dovrà essere efficiente e non far uso né di variabili globali né di parametri passati per riferimento. Infine, si scriva un algoritmo iterativo che simuli precisamente l' algoritmo ricorsivo di cui sopra.

## 2022-07-21
Si scriva un algoritmo ricorsivo che, dati in ingresso un albero binario di ricerca su interi $T$ e due valori $k_{1}, k_{2} \in N$, cancelli da $T$ le chiavi $k$ comprese tra $k_{1}$ e $k_{2}$ $(k_{1}\leq k \leq k_{2})$. Tale algoritmo dovrà essere efficiente e non far uso né di variabili globali né di parametri passati per riferimento. Infine, si scriva un algoritmo iterativo che simuli precisamente l'algoritmo ricorsivo di cui sopra.

## 2022-06-21
Si scriva un algoritmo ricorsivo che, dati in ingresso un albero binario di ricerca su interi $T$ e due valori $k_1, k_{2} \in N$, inserisca ni una lista $\mathcal{L}$  chiavi $k$ contenute in $T$ comprese tra $k_{1}$ e $k_{2} ( k_{1} \leq k ≤ k_{2})$ , in modo che al termine $\mathcal{L}$ contenga valori ordinati in modo decrescente. Tale algoritmo dovrà avere complessità lineare nella dimensione dell'albero. Infine, si scriva un algoritmo iterativo che simuli precisamente l'algoritmo ricorsivo di cui sopra.

## 2002-02-28
Sia dato un albero binario di ricerca nei cui nodi non sia presente il puntatore al padre. Si descriva prima e si sviluppi poi un algoritmo ricorsivo che realizzi la cancellazione di un nodo dell’albero (se esiste). L’algoritmo dovrà ricevere in input:
- un puntatore alla radice del (sotto)-albero su cui eseguire l’operazione di cancellazione;
- il valore della chiave (e non il nodo) da eliminare (se presente).

## 2006-06-19
Si scriva un algoritmo ricorsivo efficiente che cancelli da un albero binario di ricerca T tutte le chiavi contenute in un altro albero binario di ricerca T'.

## 2006-09-11
Si definisca un algoritmo ricorsivo efficiente che, ricevuti in ingresso un (riferimento ad un) Albero Binario di Ricerca $T$ e tre valori $k_min$, $k_max$ (con $k_min \leq k_{max}$)e $z \geq 0$ cancelli dall'albero $T$ tutti i nodi che o hanno chiave con valore esterno all'intervallo ($k_{min}, k_{max}$) o stanno a distanza maggiore uguale a z dalla radice. Non è ammesso l'uso di variabili globali né del passaggio di parametri per riferimento.

## 2007-06-25
Scrivere un algoritmo ricorsivo efficiente che, dato un albero binario di ricerca $T$ e un due valori $k_{1}$ e $k_{2}$ (con $k_{1} < k_{2}$), cancelli da $T$ tutti nodi con chiavi comprese tra $k_{1}$ e $k_{2}$ e restituisca il numero di nodi cancellati dall'albero.

## 2007-07-16
Scrivere un algoritmo ricorsivo efficiente che, dato un albero binario di ricerca $T$, due valori $k_{1}$ e $k_{2}$ (con $k_1 < k_2$) e un valore $c$, restituisca (se esiste), effettuando una sola visita dell'albero, il puntatore al nodo di $T$ che ha chiave compresa tra $k_{1}$ e $k_{2}$ e al tempo stesso che sia la più vicina possibile al (ma diversa dal) valore $c$.


## 2008-02-12
Si consideri un albero binario $T$ che soddisfa la seguente proprietà: il valore della chiave di ogni nodo è non minore del valore delle chiavi dei suoi due figli.
Si definisca un algoritmo ricorsivo che dato (il riferimento a) l'albero $T$ e due valori di chiave $k_{min}$ e $k_{max}$ (con $k_min < K_max$), cancelli dall'albero $T$ tutti i nodi con chiave compresa tra $k_min$ e $k_max,$ preservando la proprietà sopra riportata.
Suggerimento: Può risultare utile sviluppare un algoritmo ricorsivo di appoggio che esegua la cancellazione della radice di un (sotto) albero del tipo descritto sopra e ritorni l'albero risultante.

## 2008-03-27
Si definisca un algoritmo ricorsivo efficiente che, ricevuti in ingresso un (riferimento ad un) Albero Binario di Ricerca $T$ e tre valori $kmin,$ $k_max$ (con $k_min \leq K_mazx$) e $k$, restituisca, se esiste, quel nodo di $T$ che ha chiave con valore interno all'intervallo ($k_min, k_max$) e che, contemporaneamente, sia il più lontano possibile da k Non è ammesso l u'so di variabili globali né del passaggio di parametri per riferimento.


## 2008-06-20
Sia dato un albero binario di ricerca $T'$ in cui ogni nodo contiene esclusivamente un campo per la chiave, uno per il puntatore al figlio destro e uno per il figlio sinistro, Siano inoltre dati in ingresso un possibile valore di chiave $k$ e due valori $l_1$ e $l_{2}$ (con $l_{1}\leq l_{2}$ ), scrivere un algoritmo ricorsivo efficiente che cerchi e stacchi, se esiste, quel "nodo dell'albero $T'$ che, tra i nodi che si trovano ad un livello di profondità esterno all'intervallo $[l_{1}, l_{2}]$ e che sono diversi dalla radice di $T,$ contiene la chiave più vicina possibile a $k$ ma maggiore di $k$.

## 2010-01-22
Scrivere un algoritmo ricorsivo efficiente che cancelli da un Albero Binario di Ricerca $T$ (i cui nodi contengono solo il campo chiave, figlio destro e figlio sinistro) ogni nodo, diverso dalla radice dell'albero, che soddisfa la seguente proprietà:
"contiene una chiave pari minore di $k$ ed è radice di un sottoalbero di altezza minore di $H$" dove $H$ è un valore fornito in ingresso. Si noti che la proprietà dei nodi da cancellare è da intendersi rispetto all'albero originario $T$ in ingresso. Non è ammesso l'uso di variabili globali né di passaggio di parametri per riferimento.

## 2011-06-22
Sia dato un albero binario di ricerca ,$T$ i cui nodi contengano esclusivamente una chiave intera, un puntatore al figlio sinistro e uno al figlio destro.
Si definisca un algoritmo ricorsivo efficiente che, dati i valori interi $h_{2} \geq 1, h_{2} ≥ 1,k_{1} \geq 0,k_{2} \geq 0$, cancelli dall'albero $T$ tutti i nodi che, nell'albero originale fornito in ingresso, soddisfano al seguente proprietà:
hanno chiave $k$ pari tale che $k_{2}\leq k \leq k_{2}$ e sono radici di sotto-alberi li cui percorso esterno ha lunghezza $h$ che soddisfa $h_{1} \leq h \leq h_{2}$.
Si ricorda che la lunghezza del percorso esterno in un albero radicato nel nodo e è la somma delle lunghezze dei percorsi da x ad una foglia.

## 2011-07-15
Sia dato un albero binario di ricerca $T,$ i cui nodi contengano esclusivamente una chiave intera, un puntatore al figlio sinistro e uno al figlio destro. Sia dato, inoltre, un array $A$ contenente possibili chiavi intere ordinate in modo crescente.
Si definisca un algoritmo ricorsivo efficiente che cancelli dall'albero $T$ tutti i nodi che sono a distanza $h \geq 1$ dalla radice dell'albero fornito in ingresso e che contengono una chiave presente nell'array $A$ .

## 2012-03-23
 Si definisca un algoritmo ricorsivo efficiente che, dati un albero binario di ricerca $T$ (i cui nodi contengono esclusivamente un campo chiave, un campo figlio sinistro eun campo figlio destro), un intero positivo $x >0$ e un valore $k,$ cancelli da $T$ il nodo che soddisfa la seguente proprietà:
contiene la più grande chiave minore di $k$ che si trova in $T$ a profondità non minore di $x$.

## 2012-06-25
Sia dato un Albero binario Parzialmente Ordinato $T,$ in cui ogni nodo ha chiave non maggiore di quella dei suoi due figli. I nodi di $T$ contengono esclusivamente un campo chiave, un campo figlio sinistro e un campo figlio destro. Si definisca un algoritmo ricorsivo efficiente, che dati tre valori interi strettamente positivi $x, k_{1},k_{2}$ e l'albero $T$,  cancelli da $T$ ogni nodo che che soddisfa al seguente proprieta:
- contiene una chiave $k$ di valore compreso  tra $k_{1}$ e $k_{2}$ ed  è radice di un albero che contiene al massimo $x$ nodi con chiavi comprese tra $k_{1}$ e $k_{2}$

## 2012-09-11
Sia dato un albero binario di ricerca $T,$ i cui nodi contengano esclusivamente una chiave intera, un puntatore al figlio sinistro e uno al figlio destro. Si definisca un algoritmo ricorsivo efficiente che, dati cinque valori interi $h_1 ≥ 1, h_2 ≥ 1, n_1 ≥ 0, n_2 ≥ 0$ e $k,$ cancelli dall’albero $T$ tutti i nodi che, nell’albero in ingresso, soddisfano la seguente proprietà:
- ha chiave pari minore di $k,$ la sua distanza dalla radice è compresa tra i valori $h_1$ e $h_2$ ed è radice di un sottoalbero i cui nodi con chiave minore di $k$ sono in numero compreso tra $n_1$ e $n_2$ .

## 2013-09-09
Sia dato un albero binaro T(i cui nodi contengono esclusivamente un campo chiave intero, un campo figlio sinistro e un campo figlio destro).
Scrivere un algoritmo ricorsivo efficiente che elimini da T tutti i nodi che contengono una chiave pari e, contemporaneamente, costruisca un albero binario di ricerca T' contenente tutti i nodi eliminati da T. L'algoritmo richiesto deve restituire l'albero T' e non può avere T' tra isuoi parametri di ingresso.
Non è ammesso l'uso di passaggio di parametri per riferimento né l'impiego di variabili globali.

## 2014-06-26
 i a dato un Albero Binario di Ricerca ,T i cui nodi contengono i seguenti 4 campi: (2) un campo chiave di tipo intero: (zi) due campi uno per figlio sinistro e uno per figlio destro; e (iii) un campo addizionale di
tipo intero, che associa ad ogni nodo il numero di foglie contenute nel sottoalbero di cui esso è radice. Siano, inoltre, dati due interi ky e kz (con kj ≤ k2) e due interi x > 0 e h > 0. Definire un algoritmo ricorsivo efficiente che cancelli da T tutti nodi che, nell'albero iniziale T ni ingresso, soddisfano la seguente
condizione:
"hanno chiave pari compresa tra kj e kz, hanno profondità minore o uguale ad h e il percorso esterno del sottoalbero di cui sono radici è maggiore o uguale a r."
L'albero risultante deve essere dello stesso tipo dell'albero in ingresso (si faccia, quindi, attenzione a
calcolare correttamente i valori del quarto campo dei nodi).
Non è ammesso l'uso di passaggio di parametri per riferimento né l'impiego di variabili globali.

## 2014-07-18
Sia dato un albero binaro parzialmente ordinato T(in cui i figli di ogni nodo hanno chiave non maggiore di quella del nodo stesso).
A) scrivere un algoritmo ricorsivo efficiente che, dato ni ingresso T e un valore k > 0, restituisca la lista ordinata delle chiavi pari e minori di k contenute nell'albero (l'albero T non deve
essere necessariamente preservato).
B)come modifichereste la procedura del punto A) se venisse richiesto di risolvere il problema senza modificare l'albero originario T?
Non è ammesso l'uso di passaggio di parametri per riferimento né l'impiego di variabili glob- ali.

## 2015-01-29
Sia dato un albero binario di ricerca T (i cui nodi contengono esclusivamente un campo chiave di tipo intero, un campo figlio sinistro e un campo figlio destro) e due interi k1 e k2 (con k1 ≤ k2). Definire un algoritmo ricorsivo efficiente che cancelli da T tutti e soli i nodi a profondità massima con chiave pari compresa tra ki e k2. Più precisamente, l'algoritmo deve cancellare tutti e soli i nodi che soddisfano entrambe le seguenti condizioni:
(a) hanno chiave pari e compresa tra ki e k2;
(b) non hanno aleun discendente che soddisfi la condizione (a).

## 2015-02-20
 Sia dato un albero binaro di ricerca T (i cui nodi contengono esclusivamente un campo chiave intero, un campo figlio sinistro e un campo figlio destro).
Scrivere un algoritmo iterativo efficiente che costruisca una lista ordinata (in ordine cres- cente), contenente tuti inodi di Tel cui chiavi siano contenute nell'intervallo di interi [ky,]ak eche is trovino aprofondità comprese nel'intervalo di interi [/1a/]4,d(ove ,T kyka,. h, ezh sono tutti parametri di input dell'algoritmo).

## 2016-03-23
Sia dato un albero binaro di ricerca $T$ ( i c u i n o d i contengono esclusivamente un campo chiave, un campo figlio sinistroeuncampofigliodestro)eunarrayordinato Acontenente m chiavi. Scrivere un algoritmo ricorsivo efficiente che inserisca nell'albero T tutti le chiavi di Ache non siano già presenti in T.
