---
author: Lorenzo Tecchia
tags:
  - definition
  - algorithm
  - operation/graph
  - to-do/implementation
---
[[Algoritmo]] che determina se un [[grafo]] è ***aciclico*** (non ha [[Cycle|cicli]])
	
```python
def Acyclic(G):
	color = Init(G)
	for v in V:
		if color(v) == bn:
			acyclic = DFSAcyclic(G, v, color)
			if !acyclic:
				return False
	return True
```
^acyclic

```python
def DFSAciclic(G, v, color):
	color(v) = gr
	for w in Adj[v]:
		if color(w) = bn:
			acyclic = DFSAciclic(G,v, c)
			if !aciclic:
				c(v) = nr
				return False
		else if c(w) = gr:
			return False
	color(v) = nr
	return True				
			
```
^dfs-acyclic

### La struttura è identica ad una $\textbf{DFS}$.
- Inizializza il colore di tutti i vertici a **bianco**.  
- Controlla ogni vertice non scoperto (**bianco**) del grafo, se solo uno di questi trova un **ciclo**, il grafo non è **aciclico** e restituisce `FALSE`.
- Controllati tutti i vertici, se nessuno di questi ha trovato un ciclo, allora il grafo è **aciclico** e restituisce `TRUE`
### $\textbf{DFSAcyclic}$:  
Il vertice $v$ è stato scoperto, quindi viene colorato di **grigio** e viene esplorata la stella uscente:
- se il nodo adiacente $w$ è **bianco**, allora scende ricorsivamente in $w$  
- se il nodo adiacente $w$ è **grigio**, allora è stato incontrato un nodo che è stato già visitato durante la discesa, ***quindi è stato trovato un ciclo***
### $\textbf{DFSAcyclic}$:
- Nel caso migliore, impiega tempo costante $\varOmega(1)$ 
- Nel caso peggiore, impiega $O(|G|)$

## Implementazione
```C
//da implementare
```
