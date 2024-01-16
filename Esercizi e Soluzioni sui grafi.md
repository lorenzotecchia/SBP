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
	Init(G); 
	Q = Enqueue(Q, v)
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

### 2018-06-28
Sia dato un grafo orientato $G = <V, E>$, rappresentato con liste di adiacenza, e un array $A$ contenente un sottoinsieme dei vertici di $G$ (quindi , $A \subseteq V$). Si scriva un algoritmo che, dati in ingresso $G, A$ e un vertice $v \in V$, calcoli in **tempo lineare sulla dimensione di $G$**, l'insieme dei vertici $Z \subseteq V$ contenente **tutti e soli** i vertici di $G$ che soddisfano la seguente condizione:
- $z \in Z$ se e solo se esiste un percorso in $G$ da $z$ a $v$ che passa per un qualche $a \in A$ (non fornito in ingresso), cioè se esiste $a \in A$ tale che $z \leadsto a \leadsto v$ (dove $x \leadsto y$ indica che $x$ raggiunge $y$ tramite un qualche percorso)
#### Esecuzione-Lorenzo
```python
def Algo(G, A, v):
	Init(G, color1, color2)
	Z = NULL	
	G_t = Transpose(G)
	DFS(G, color1)
	DFS_Visit(G_t, v, color2)
	for a in A:
		if color1[a] == color2[a]:
			Z.append(a)
	return Z

def DFS(G):
	for v in G.V:
		if color[v] == B:
			color = DFS_Visit(G, v)
	return color	

def DFS_Visit(G, s):
	color[s] = G
	for u in Adj[v]:
		if color[u] == B:
			color = DFS_Visit(G, w)
	color[w] = N

def Init(G):
	for v in G.V:
		color[w] = B

def Transpose(G):
	V_t = G.V
	for v in G.V:
		E_t = Insert(G)
```
#### Esecuzione-Eserciziario
```python
def Algot(G, A, v):
	Z = NULL
	Init(G, c1, c2)
	BFS(G_t, v, c1)
	for a in A:
		if c1[a] == N:
			DFS_Visit(G_t, a, c2)
	for u in V:
		if c2[v] == N:
			Z.append(u)
```

### 2018-01-25
Dati in ingresso un grafo $G$ e tre vertici $s, v, u$ si vuole verificare, in tempo lineare sul grafo $G$, se esiste un percorso in $G$ che parte da $s$, passa per $v$ ma non per $u$
#### Esecuzione
```python
def Algo(G, s, u, v):
	Init(G)
	color[u] == N
	color = DFS_Visit(G, s)
	# sbagliato
	if color[v] == N:
		return True
	return False

def DFS_Visit(G, x):
	color[x] = B
	for y in Adj[x]:
		if color[y] == B:
			color = DFS_Visit(G, y)
	color[x] == N
	return color
```
#### Esecuzione-Eserciziario
```python
def Algo(G, s, u, v)
	Init(G)
	color[u] = N
	BFS(G, s)
	return color[v] == N
```

### 2018-07-24
Sia dato un grafo orientato $G$, rappresentato con liste di adiacenza, e due array $A$ e $B$, ciascuno contenente un sottoinsieme dei vertici di $G$ (quindi, $A \subseteq V$ e $B \subseteq V$). Si scriva un algoritmo che, dati in ingresso $G, A, B$ calcoli in **in tempo lineare sulla dimensione del grafo** $G$ l'insieme dei vertici $Z \subseteq V$ contenente **tutti e soli** i vertici di $G$ che soddisfano la seguente condizione:
- $z \in Z$ se e solo se esistono in $G$ due percorsi da $z$, tali che: uno porta a un qualunque vertice $a \in A$ e non passa per alcun vertice di $B$; l'altro porta a un qualunque vertice $b \in B$ e non passa per alcun vertice di $A$.

```python
def Algo(G, A , B) 
	Z = NULL
	Init(G, B, color1) # tutti i colori di bianco tranne b in B di nero
	for a in A:
		if color1[a] == B:
			DFS_Visit(G_t, a, color1)
	Init(G, A, color2) # tutti i colori di bianco tranne a in A di nero
	for b in B:
		if color2[b] == B:
			DFS_Visit(G_t, b, color2)
	for z in V:
		if color1[z] == N && color2[z] == N:
			Z.append(z)
	return Z

def Init(G, A):
	for v in G.V-A:
		color[v] == B
	for x in A:
		color[x] == N

def DFS_Visit(G, s)
	color[s] = G
	for t in Adj[s]:
		if color[t] == B:
			color = DFS_Visit(G, t)
	color[s] = N
	return color
```

### 2019-07-03
Sia dato un grafo non orientato $G$, rappresentato con liste di adiacenza. Si scriva lo pseudo-codice di un algoritmo che, dato in ingresso unicamente $G$, verifichi in tempo lineare sulla dimensione di $G$ se è possibile partizionare l'insieme di vertici in due insiemi $V_{1}\subseteq V$ e $V_{2} \subseteq V$ che soddisfano le seguenti condizioni:
- $V = V_{1} \cup V_{2}$
- $V_{1} \cap V_{2} = \emptyset$
- $v \in V_{1}$ se e sole se per ogni arco $(v,u) \in E$ vale $u \in V_{2}$
In casso affermativo. l'algoritmo deve fornire i due insiemi $V_{1}$ e $V_{2}$ risultanti
#### Esecuzione
```python
def Algo(G):
	Init(G)
	for v in G.V:
		color1 = BFS_Mod(G, v)

def BFS_Mod(G, v):
	Q = Enqueue(Q, s)
	while Q != NULL:
		v = Head(Q)
	for u in Adj[v]:
		if color[v] == B:
			color[u] = N
		if color[v] == N:
			color[u] = B
		Q = Enqueue(Q, u):
		# DA RIVEDERE
```
### 2019-02-12
Si scriva un algoritmo che, dato in ingresso un grafo orientato $G$, in valore intero $k$, un vertice $s \in V$ e un insieme $A \subseteq V$ rappresentato come array di vertici, verifichi, **in tempo lineare sulla dimensione del grafo**, se è vera la seguente condizione:
_ogni percorso che parte dal vertice $s$ e raggiunge un qualche vertice di $A$ ha lunghezza maggiore di $k$_
#### Esecuzione
```python
def Algo(G, k, s, A): # dobbiamo verificare che esiste un percorso che parte da s ed arriva ad a 
	(color,discovery) = BFS(G, s)
	for a in A:
		if color[a] == N && discovery[a] <= k:
			return False
	return True

def BFS(G, v):
	Init(G, color, discovery) # inizializziamo discovery[v]
	Q = Enqueue(v):
	while Q != NULL:
		v = Head(Q)
		for u in Adj[v]:
			if color[v] == B:
				Q = Enqueue(Q, u)
				color[u] = G
				discovery[u] = discovery[v] + 1
		color[v] = N
	return discovery, color
		
```

### 13-01-2021

 Sia dato un grafo orientato  $G$, rappresentato con liste di adiacenza, e un vertice $s$
 e due insiemi di vertici $B \subseteq V$ e $C \subseteq V$, rappresentati come array.
 Si scriva un algoritmo che, dati in ingresso $G, s, B, C$, collezioni in tempo lineare
 sulla dimensione di $G$ in una lista $L$ tutti i vertici $v$ che soddisfano  entrambe
 le seguenti condizioni:
 - $v$ appartiene a $B$ e può raggiungere $s$ tramite un percorso
 - esiste anche un percorso da $s$ a $v$ che non passa per alcun vertice di $C$

#### Esecuzione
```python
def Algo(G, s, B, C)
	L = NULL
	Init(G, color1, color2) # in color2 tutti a bianco tranne per ogni c in C imposto i colori a Nero
	G_t = Transpose(G)
	color1 = DFS_visit(G_t, s)
	color2 = DFS_visit(G, s)
	for b in B:
		if color1[b] == N && color2[b] == N:
			L.append(b)
	return L

def DFS_Visit(G, s)
	color[s] = G
	for v in Adj[s]:
		if color[v] == B:
			color = DFS_Visit(G, v)
	color[s] = N

def Transpose(G):
	G_t.V = G.V
	for v in G.V:
		for w in Adj[v]:
			E_t = Insert(E_t, (w, v))
	return G_t
```

### 22-02-2021
