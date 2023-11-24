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

#### Corollario 1
Dato un grafo pesato $G =(V, E, w)$ e sia  $π=v_1v_{2\dots}v_{k-1}v_k$ un percorso minimo da $v_1$ a $v_k$ , allora  $\delta(v_1, v_k)\leq\delta(v_1, v_{k-1})+w(v_{k-1}, v_k)$

#### Lemma 2
Dato un grafo pesato $G =(V, E, w)$ e $s \in V$. Per ogni arco $(u, v)\in E$ vale che:
$\delta(s, v)\leq\delta(s, u)+w(u, v)$.

#### Lemma 3
Dato un grafo pesato $G =(V, E, w)$ e  un arco $(u, v) \in E$, immediatamente dopo l'esecuzione di $Relax(u, v, w)$ varrà che: $d[v]\leq d[u]+ w(u, v)$.

#### Lemma 4
Dato un grafo pesato $G =(V, E, w)$ e posti $d[v]= \infty$,  $\forall v \in V \setminus \{s\}$ e $d[s] = 0$ lungo una qualsiasi sequenza di operazioni di rilassamento vale sempre: $d[v]\geq \delta(s, v)$  $\forall v \in V$



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
