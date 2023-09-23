---
author: Lorenzo Tecchia
tags:
  - algorithm
  - to-do/implementation
---
The ***Kruskal*** algorithm finds a [[Minimum Spanning Tree#^509260|minimum spanning forest]] for an [[undirected]] edge-
weighted-[[graph]]. If the graph is connected, it finds a [[minimum spanning tree]]. 

It is a [[greedy]] algorithm in graph theory as in each step it adds the next lowest-weight edge that will not form a cycle to the minimum spanning forest.

## proceeding of the algorithm
- Create a [[forest]] F, where each vertex in the graph is a separate tree.
- Create a sorted [[Fundamentals#set|set]] S containing all the edges in the graph
- While S is nonempty and F is not yet spanning
	- Remove an edge with minimum weight from S
	- If the removed edge connects two different trees then add it to the forest F, combining two trees into a single tree

At the termination of the algorithm, the forest forms a minimum spanning forest of the graph. If the graph is connected, the forest has a single component and form a minimum spanning tree.

## pseudocode
```pseudo
	\begin{algorithm}
	\caption{Kruskal Algorithm}
	\begin{algorithmic}
	\end{algorithmic}
	\end{algorithm}
```
```
F := emptySet
for each v in G.V do
	MAKE_SET(v)
for each (u, v) in G.E ordered by weight(u, v) increasing do
	if FIND-SET(u) not_equals FIND-SET(v) then
		F := F union {(u, v)} union {(u, v)}
		UNION(FIND-SET(u), FIND-SET(v))
return F
```

## [[Complexity]]
For a graph with E edges and V vertices, Kruskal algorithm can be shown to run in $O(E\  logE)$ time, or equivalently, $O(E\ logV)$ time, all with simple data structures.

## [example](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm#Example)

## Implementazione
```C
// da implementare
```
