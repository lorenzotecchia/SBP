---
author: Lorenzo Tecchia
---
### 2017-07-17
Si scriva un algoritmo che, dato come unico input un grafo orientato $G=(V, E)$, verifichi in tempo lineare sulla dimensione di $G$ se esistono tre vertici $a,b,c \in V$ tali che **almeno una** delle seguenti condizioni è verificata:
- $a$ non raggiunge $b$, oppure
- $b$ non raggiunge $c$, oppure
- $a$ non raggiunge $a$
#### Esecuzione
```python
def Algo(G):
	Init(G, c1, c2, c3)
	for each a,b,c in V do:
		DFS_Visit(G, a, c1)
		DFS_Visit(G, b, c2)
		DFS_Visit(G, c, c3)
		if c1[b] == B || c2[c] == B || c3[a] == B:
			return True
	return False
```

### 2018-02-23
Siano dati un grafo $G = (V, E)$, due insiemi di vertici $A \subseteq V$ e $B \subseteq V$ (entrambi rappresentati come array) e un intero $k$. Si vuole verificare in tempo **lineare sulla dimensione del grafo** $G$, se ogni percorso che parte da un vertice in $A$ e raggiungere un vertice in $B$ ha lunghezza maggiore o uguale a $k$
Si illustri brevemente a parole l'idea della soluzione che si intende proporre e spieghi perché risolve il problema in tempo lineare. Successivamente, si scriva l'algoritmo che risolve il problema.
#### Esecuzione
```python
def Algo(G, A, B, k):
	for x in A:
		if color[x] == B:
			discovery, color = BFS(G, x)
	for y in B:
		if color[y] == N && discovery[y] <= k:
			return False
	return True

def BFS(G, v):
	Init(G); Q = Enqueue(Q, v)
	color[v] = G
	discovery[v] = 0
	while Q != NULL:
		(Q,v) = Head&Dequeue(Q)
		for u in Adj[v]:
			if color[u] == B:
				Q = Enqueue(Q, u)
				color[u] = G
				discovery[u] = discovery[v] + 1
		color[v] = N
	return color, discovery
```