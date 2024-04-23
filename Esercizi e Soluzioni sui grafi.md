---
author: Lorenzo Tecchia
tags:
  - algorithm
  - graph
---
### 2017-07-18
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
	V1 = GeneratoreInsiemeCasuale(V)
	V2 = V - v1
	for v in V:
		if v in V1:
			colore(v) = Giallo
		else:
			colore(v) = Verde
	for v in V1:
		if v in Adj(u) && colore(v) != Verde
			V1 = V1 - {u}
			V2 = V2 + {u}

def GeneratoreInsiemeCasuale(V):
	return V/2
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

### 2019-09-04
Dato $G$ e $A \subseteq V$ calcola l'insieme $Z \subseteq A$ t.c. $\forall z \in A \;\; z \in Z \iff$ ogni percorso che parte da $u$ e raggiunge  $v$ non passa per $z$

#### Esecuzione
```python
def Algo(G, A, u, v):
	Z = empty
	(color1, color2) = Init(G)
	G_t = Transpose(G)
	color1 = DFS_Visit(G, u, color1)
	if color1(v) == N:
		color2 = DFS_Visit(G_t, v, color2)
		if color2(u) == N:
			for a in A:
				if color2(a) == B or color1(a) == B:
					Z = Z + {a}
	return Z
```

### 2019-03-29A
Dato $G$ e $A \subseteq V$ e due vertici $u,v$ scrivere un algoritmo che calcoli $A' \subseteq A$ t.c $\forall a' \in A\;\;\; a \in A' \iff$ esiste un percorso che parte da $u$, arriva a $v$ passando per $a$.
#### Esecuzione
```python
def Algo(G, A, v, u):
	A' = empty
	(color1, color2) = Inti(G)
	G_t = Transpose(G)
	(color1) = DFS_Visit(G, u, color1)
	if color1(v) == N:
		color2 = DFS_Visit(G, v, color2)
		if color2(u) == N:
			for a in A:
				if color1(a) == N && color2(a) == N:
					A' = A' + {a}
	return A'
```


### 2019-03-29B
Dato $G$ e $B \subseteq V$ e due vertici $u,v$ e un intero $k$, scrivere un algoritmo che determini l'insieme $B' \subseteq B$ t.c. $\forall b \in B$
$b \in B'\iff b$ è raggiungibile da $v$ senza passare per $u$ e $b$ raggiunge $u$ con un percorso lungo $< k$

#### Esecuzione
```python
def Algo(G, B, u, v, k):
	B' = empty
	color1 = Init(G, u) # colora tutti a bianco tranne u a nero
	color2 = Init(G)
	color = BFS(G, v, color)
	for b in B:
		if color(b) == N:
			color2 = BFS(G, b, color2)
				if color2(u) == N && discovery(v) < k:
					B' = B' + {b}
	return B'
```

#### Esecuzione Eserciziario
```python
def Algo(G, B, u, v, k):
	B' = empty
	(color1, color2) = Init(G)
	color1(u) = N
	DFS_Visit(G, v, color1)
	G_t = Transpose(G)
	color2 = BFS(G_t, u, color2)
	for b in B:
		if color1(b) == N && color2(b) == N && discovery(b) < k:
			B' = B' + {b} # dove per + è l'unione insiemisticaA
	return B
```
### 2019-06-13
Si consideri un grafo $G$ i cui nodi rappresentano dei corsi e gli archi i vincoli di propedeuticità per i relativi esami. Scrivere un algoritmo che, dato $G$, calcoli il numero minimo di semestri necessari per completare tutti i corsi, se ogni corso è semestrale

#### Esecuzione
```python
def Algo(G):
	color = Init(G)
	S = DFS(G, color)
	for s in S:
		counter = counter + q
	return counter
	
def DFS(G, color):
	S = NULL
	for v in V:
	if color(v) == B:
		S = DFS_Visit(G, v, color, S)
	return S

def DFS_Visit(G, v, color, S):
	color(v) = G
	for u in Adj(v):
		if color(v) == B:
			S = DFS_Visit(G, u, color, S)
	color(v) = N
	push(S, v)
	return S
```
### Sconosciuta
Dato $G, s \in V,\;\; B, C \subseteq V$ scrivere un algoritmo che collezioni in una lista tutti i vertici $v \in V$ t.c.
- $u \in B$ e raggiunge $s$
- esiste un percorso da $s$ a $v$ che non passa per alcun vertice di $C$

#### Esecuzione
```python
def Algo(G, s, B, C):
	L = empty
	(color1, color2) = Init(G)
	for c in C:
		color2(c) = N
	for b in B:
		color1 = BFS(G, b, color1)
		if color1(s) == N:
			color2 = DFS(G, s, color2)
			if color2(b) == N:
				L = L + {b}
	return L
```
#### Esecuzione Eserciziario
```python
def Algo(G, s, B, C):
	L = empty
	Init(G, C, c1, c2) # tutti i nodi in C a nero
	DFS_Visit(G_t, s, c1)
	for b in B:
		if c1(b) == N:
			DFS_Visit(G, s, c2)
			if c2(b) == N:
				Insert(L, b)
	return L
```

### Sconosciuta
Dato $G$, verifiche se esistono tre vertici $a,b,c$ tale che:
- $a$ non raggiunge b
- $b$ non raggiunge c
- $c$ non raggiunge a

#### Esecuzione
```python
def Algo(G):
	(c1, c2, c2) = Init(G)
	for a, b, c in V:
		c1 = DFS_Visit(G, a, c1)
		c2 = DFS_Visit(G, b, c2)
		c3 = DFS_Visit(G, c, c3)
		if c1(b) == B && c2(c) == B && c3(a) == B:
			return True
	return False
```

### Sconosciuta
Dato $G$ e $X \subseteq V$ e due vertici $u,v$ scrivere un algoritmo che verifica le seguenti proprietà:
- Ogni percorso da $v$ a $u$ passa per un vertice di $X$
- Ogni percorso da $u$ a $v$ passa per un vertice di $X$

#### Esecuzione
```python
def Algo(G, X, u, v):
	(color1, color2) = Initi(G)
	G_t = Transpose(G)
	color1 = DFS_Visit(G, v, color1)
	color2 = DFS_Visit(G, u, color2)
	for x in X:
		if color1(x) == N && color2(x) == N:
			return True
	return False
```

#### Esecuzione Eserciziario
```python
def Algo(G, X, u, v):
	Init(G, c1, c2, X)# tutti bianchi tranne x in X
	DFS_Visit(G, v, c1)
	DFS_Visit(G, u, c2)
	if c1(u) == N || c2(v) == N:
		return False
	else:
		return True
```

L'euristica è: 
$\text{Esiste un per corso da }v\; \text{a } u \;\text{che non passa per } X$
oppure 
$\text{esiste un percorso da } u\; \text{a }v\; \text{che non passa per }X$
1. Annerisco quelli di X per la prima e seconda visita
2. Se esiste $u \leadsto v$ o $v \leadsto u$, `ret False`

### Sconosciuta
Dato $G$ e $A \subseteq V$ ed un vertice $v$, scrivere un algoritmo che calcola  $Z \subseteq V$ tale che $\forall z \in V$
$z \in Z \iff$ esiste un percorso da $z$ a $v$ che, prima di raggiungere $v$,  passa per almeno un vertice di $A$

#### Esecuzione
```python
def Algo(G, A, v):
	Z = empty
	Init(G, c1, c2)
	DFS_Visit(G_t, z, c1)
	for y in A:
		if c1(y) == N:
			DFS_Visit(G_t, y, c2)
	for x in V:
		if c2(x) == N:
			z = Z + {x}
	return Z
```

### Sconosciuta
Dato $G$ e $A \subseteq A$, scrivere un algoritmo che calcola l'insieme $Z \subseteq A$ tale che $\forall z \in A$
$z \in Z \iff$ ogni percorso $u \leadsto v$ non passa per $z$

#### Esecuzione
```python
def Algo(G, A):
	(color) = Init(G, A) # tutti a bianco tranne A
	DFS_Visit(G, u)
	if color(y) == N:
		for z in Z:
			if color(z) == N:
				Z = Z - {z}
	return Z
```
Ragioniamo al contrario: $A \leadsto z$ e voglio gli elementi tale che esiste un percorso $u \leadsto v$ che passa per $z$.
### Sconosciuta
Dato $G$ e tre vertici $a, b, c$ scrivere un algoritmo che verifica l'esistenza di un percorso infinito $\pi$ tale che contiene $a, b, c$.

#### Esecuzione
```python
def Algo(G, a, b, c):
	color = Init(G)
	S = DFS(G)
	G_t = Transpose(G)
	scc = DFS_scc(G, S)
	if scc(a) == scc(b) && scc(b) == scc(c):
		return True
	return False
## Scrivere algo CFC	
```

### 2017-06-28
Dato un grafo e tre vertici $a, b, c$ scrivere un algoritmo che verifica se esiste un percorso infinito che passa solo una volta prima per $a$, poi per $b$ e poi per $c$, cioè $\iff$ i tre vertici $a, b, c$ vengono incontrati un'unica volta e nell'ordine stabilito lungo qualche percorso infinito

#### Esecuzione
```python
def Algo(G, a, b , c):
	(c1, c2, c3) = Init(G)
	DFS_Visit(G, a , c1)
	DFS_Visit(G, b, c2)
	if c1(b) == N && c2(c) == N:
		return DFS_Visit_Mod(G, c, c, color)
	return TrueType

def DFS_Visit_Mod(G, v, c, color):
	color(v) = G
	for u in Adj(v):
		if color(u) == B:
			ret = False
			DFS_Visit_mod(G, u, color)
		if color(u) == G && u != c:
			ret = True
	color(v) = N
	return ret
```


### 2021-01-133

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

### 2021-02-22
Dato un grafo $G$ e due vertici $u,v$ e un insieme $A \subseteq V$, calcoli l'insieme $z$ tale che $z \in Z \iff$:
- $z \in A$
- Ogni percorso che parte da $u$ e raggiunge $v$ non passa per $z$

```python
def Algo(G, u, v, A):
	Z = A
	G_t = Transpose(G)
	(color1, color2) = Init(G, A) # tutti a bianco tranne a \in A a nero
	color1 = DFS_Visit(G, u, color1)
	color2 = DFS_Visit(G, v, color2)
	for z in Z:
		if color1(z) == N && color2(z) == N:
			Z = Z - {z}
	return Z
```
Rimuovo da $Z$ gli elementi di $A$ tali che esiste un percorso da $u$ a $v$ che passa per $Z$.

### 2021-04-13
Dato un grafo e $A \subseteq$ scrivere un algoritmo che stampa, se esistono, i due insemi $B, C \subseteq V$ tale che:
- $B \cap C \subseteq A$ cioè hanno solo i vertici di A in comune
- Ogni vertice $v \in B$ ha un percorso che raggiunge almeno un vertice in $A$
- Ogni vertice $v \in C$ è raggiungibile da almeno un vertice in $A$.
Se gli insiemi non esistono, l'algoritmo deve segnalare l'assenza di una successione.

#### Esecuzione
```python
def Algo(G, A):
	B = C = empty
	(color1, color2, color3) = Init(G, A) # tutti bianchi tranne A a verde
	G_t = Transpose(G)
	for a in A:
		color1 = DFS_Visit(G_t, a, color1)

	for a in A:
		color2 = DFS_Visit(G, a , color2)

	for v in V:
		if color1(v) == N:
			B = B + {v}
		if color2(v) == N:
			C = C + {v}

	for v in V:
		if color1(v) == N  && color2(v) == N && color3(v) != V:
			print "I due insiemi non esistono" 
			return False
	return True 
			return FalseFalsee
	return True
```

### 2021-04-13A
Dato come unico input un grafo $G$, scrivere un algoritmo che verifica l'esistenza di due vertici $a,b \in V$ tali che almeno una delle seguenti è vera:
- $a$ non raggiunge $b$, oppure
- $b$ non raggiunge $a$

### Esecuzione
```python
def Algo(G)
	color = Init(G)
	S = DFS_Stack(G, color)
	G_t = Transpose(G)
	scc = DFS_Scc(G_t, S, color)
	for a, b in V:
		if scc(a) != scc(b):
			return True
	return False
```

### 2020-02-05
Dato $G$, un array $A$ tale che $|A| \leq |V|$ tale che $A[i] \in V$ per ogni $i \in \{1, \dots, k\}$ ed un vertice $v$, scrivere un algoritmo che dati in ingresso $G, A, v$ calcoli l'insieme $Z\subseteq V$ tale che:
$z \in Z \iff$ esiste un percorso da $z$ a $v$ che prima di raggiungere $v$ passa per almeno un vertice di $A$.

#### Esecuzione
```python
def Algo(G, A, v):
	Z = empty
	(color1, color2) = Init(G, A) # tutti a bianco tranne A a nero
	G_t = Transpose(G)
	color1 = DFS_Visit(G_t, v, color1)
	for ele in A:
		if color1(A(ele)) == N:
			color2 = DFS_Visit(G, A(ele), color2)
			if color2(v) == N:
				Z = Z + A(ele)
	return Z
```

#### Esecuzione Eserciziario
```python
def Algo(G, A, v):
	Z = empty
	Init(G, c1, c2)
	DFS_Visit(G_t, v, c1)
	for a in A:
		if c1(a) == N:
			DFS_Visit(G_t, a, c2)
	for v in V:
		if c2(v) == N:
			Z = Z + {u}
	return Z
```

- Verifico chi tra $A$ raggiunge $v$
- Verifico chi tra $A$ è raggiungibile da $z$
- Il sistema dovrà $z\leadsto a \leadsto v$

### 2020-01-13
Dato $G$ e $X \subset V$ e $v, u \in V$ scrivere un algoritmo che verifichi se le sequenze sono soddisfate:
- Ogni percorso che parte da $u$ e termina in $v$ passa per qualche $x \in X$
- Ogni percorso che parte da $v$ e termina in $u$ passa per qualche $x \in X$

#### Esecuzione
```python
def Algo(G, X, u, v):
	(color1, color2) = Init(G, X)# tutti a bianco tranne x a nero
	color1 = DFS_Visit(G, u, color1)
	if color1(v) == N:
		color2 = DFS_Visit(G_t, v, color2)
		if color2(u) == N:
			return False
	return True
```

### 2017-02-24
Dato $G$ e $B \subseteq V$ scrive un algoritmo che verifichi l'esistenza di un percorso infinito $\pi$ nel quale ciascun vertice di $B$ occorre infinite volte

#### Esecuzione
```python
def Algo(G, B):
	color = Init(G)
	G_t = Transpose(G)
	S = DFS_Stack(G, color)
	scc = DFS_scc(G, S, color)
	for b,c in B:
		if scc(b) != scc(c):
			return False
	return True
```

### 2017-01-26
Dato $G$ scrivere un algoritmo che verifichi l'esistenza di due vertici $u,v$ tali che ogni percorso che parte da $u$ non passa per $v$.

#### Esecuzione
```python
def Algo(G):
	color = Init(G)
	for u, v in V:
		color = DFS_Visit(G, u, color)
		if color(v) == B:
			return True
	return False
```

### Sconosciuto
Dato $G$ e $A \subseteq V$ scrivere un algoritmo che verifichi l'esistenza di un percorso $\pi = v_{1}\leadsto v_{2}\leadsto \dots \leadsto v_{1}$ tale che $\{v_{1}, \dots , v_{n}\} \subseteq A$

#### Esecuzione
```python
def Algo(G, A):
	color = Init(G, A) # tutti a nero tranne i vertici di A
	for a in A:
		if DFS_Visit(G, a, a):
			return True
	return False

def DFS_Visit(G, v, a):
	color(v) = G
	for u in Adj[v]:
		if color(u) == B:
			return DFS_Visit(G, u, a)
		if color(u) == G && u == a:
			return True
	color(v) = N
	return False
```