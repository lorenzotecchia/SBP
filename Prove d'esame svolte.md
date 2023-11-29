## Prova d'esame 23/02/2018 

#### Esercizio 2
Dati G =(V, E) e $A, B\subseteq V$  e $k \in N$, si verifichi in tempo lineare sulla dimensione del grafo G, se ogni percorso che parte da un vertice in A e raggiunge un vertice in B ha lunghezza maggiore o uguale di k.
##### Ragionamento
L'idea è quella di restituire FALSE quando esiste $π: a\rightarrow b$ tale che la sua lunghezza è minore di k, usando una variante della BFS.

#### Soluzione
```python
def Init(G):
	for v in V:
		color[v]= B
		pred[v] = NULL
		d[v] = ∞
```

```python
def VarianteBFS(G,s,Q):
	Init(G)
	Q = {s}
	color[s] = G
	while Q != ø:
		x = Dequeue(Q)
		for u in Adj[x]:
			if color[u] == B:
				Enqueue(Q,u)
				color[u] = G
				pred[u] = x
				d[u] = d[u] + 1
		color[x] = N
```

```python
def Algo(G,A,B,k):
	for a in A:
		if color[a] == B:
			VarianteBFS(G,a)
	for b in B:
		if color[b] == N:
			if d[b] < k:
				return False
	return True
```

Non è lineare?

---
