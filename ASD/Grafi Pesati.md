---
author: Giulia Gargiulo
tags:
  - algorithm
  - definition
  - dataStructure
  - operation/graph
---
Un grafo pesato è un grafo $G =(V, E, w)$, dove  $w: E\rightarrow \mathbb{R}$ è una funzione che associa un numero reale chiamato peso ad ogni arco.
Sia $π=v_1v_{2\dots}v_{k-1}v_k$ un percorso in G, allora il peso di questo percorso è uguale a : $$w(π)=\sum_{i=1}^{k-1}\limits w(v_i,v_{i+1})$$
Definiamo il peso del percorso minimo da $u$  a $v$ : 
$$\delta(u, v) = \begin{cases}\min \{w(p): u \rightarrow v\} & \text { se esiste un percorso da u a v}\\ \infty & \text { altrimenti }\end{cases} $$

Un percorso minimo da $u$ a $v$ è un qualsiasi percorso con peso $w(p)=\delta(u, v)$

##### Operazione di rilassamento

```python
def Relax(u, v, w):
	if d[v] > d[u] + w(u, v):
		d[v] = d[u] + w(u, v)   # aggiorno la stima
		Pred[v] = u
```

Viene eseguito in tempo costante

---
#### Lemma 1
Dato un grafo pesato $G =(V, E, w)$ e sia  $π=v_1v_{2\dots}v_{k-1}v_k$ un percorso minimo da $v_1$ a $v_k$ in G, $\forall 1 \leq i  \leq j  \leq k$,  $π_{ij} =v_iv_{i+1}\dots v_j$ è il percorso minimo da $v_i$ a $v_j$.

>[!note] 
> Ogni percorso minimo tra due vertici contiene a sua volta percorsi minimi.

---
#### Corollario 1
Dato un grafo pesato $G =(V, E, w)$ e sia  $π=v_1v_{2\dots}v_{k-1}v_k$ un percorso minimo da $v_1$ a $v_k$ , allora  $\delta(v_1, v_k)\leq\delta(v_1, v_{k-1})+w(v_{k-1}, v_k)$


---
#### Lemma 2
Dato un grafo pesato $G =(V, E, w)$ e $s \in V$. Per ogni arco $(u, v)\in E$ vale che:
$\delta(s, v)\leq\delta(s, u)+w(u, v)$.

---
#### Lemma 3
Dato un grafo pesato $G =(V, E, w)$ e  un arco $(u, v) \in E$, immediatamente dopo l'esecuzione di $Relax(u, v, w)$ varrà che: $d[v]\leq d[u]+ w(u, v)$.

---
#### Lemma 4
Dato un grafo pesato $G =(V, E, w)$ e posti $d[v]= \infty$,  $\forall v \in V \setminus \{s\}$ e $d[s] = 0$ lungo una qualsiasi sequenza di operazioni di rilassamento vale sempre: $d[v]\geq \delta(s, v)$  $\forall v \in V$

#### Dimostrazione
Dimostrazione per induzione sul numero delle operazioni di rilassamento $i$:
-Caso base : $i =0$, è ovvio, perchè non viene eseguita nessuna operazione di rilassamento.
-Caso induttivo: $i >0$, prima della $i-esima$ operazione vale ,per ipotesi induttiva, che: $\forall v \in V, \ d[v]\geq\delta(s, v)$

Consideriamo un arco $(x, y)\in E$, su cui eseguo $Relax(x, y, w)$; poichè l'operazione di rilassamento modifica soltanto $d[y]$, sicuramente $\forall v \in V \setminus\{y\}$vale: $d[v]\geq\delta(s, v)$

Due casi:

---
#### Corollario 2
Siano $s,v \in V$ e sia $s$ la sorgente. Se $v$ è raggiungibile da $s$, in ogni momento lungo una sequenza arbitraria di rilassamenti vale: $d[v]=\delta(s, v)$.
Consideriamo le stime iniziali: $d[s]=0,\ d[v]=\infty$

Di conseguenza, se $v$ non è raggiungibile da $s$, allora $\delta(s, v)=\infty$ e $d[v]\geq\delta(s, v),\ \forall v \in V$

---
#### Lemma 5
Dato un grafo pesato $G =(V, E, w)$ e sia $π=v_1v_{2\dots}v_{k-1}v_k$ un percorso minimo da $v_1$ a $v_k$, inizializzando $d[s]= 0,\ d[v]=\infty$. Presa un'arbitraria sequenza di rilassamento che contiene $Relax(v_{k-1},v_k,w)$, se prima dell'esecuzione di $Relax$ $d[v_{k-1}]=\delta(s, v_{k-1})$, allora dopo l'esecuzione di $Relax$ vale: $d[v_k]=\delta(s, v_k)$

---
#### Algoritmo di Bellman-Ford
```python
def Bellman_Ford(G, s):
	Init(G, s)
	for i == 1 in range (|V|-1):
		for (u, v) in E:
			Relax(u, v, w)
	for (u, v) in E:
		if d[v] > d[v] + w(u, v):
			return False
	return True
```
---
#### Algoritmo di Dijkstra
```python
def Dijkstra(G, s):
	Init(G, s)
	S = ø
	Q = V 
	while Q != ø:
		u = Extract_Min(Q)
		S = S ∪ {u}
		Q = Q - {u}
		for v in Adj[u]:
			Relax(u, v, w)
```
