---
tags: [example, exercise]
author: Lorenzo Tecchia
---
# Esercitazioni varie sulle DFS 
Tutte gli pseudo codice verranno scritti da me con python

## Spiego la logica dietro la DFS come se lo stessi spiegado a voce in questo piccolo riassunto
La DFS è un algortimo atto all'esplorazione di un grafo, o per lo meno a la verifica di una certa proprietà presente all'interno del grafo per mezzo di un visita "in profondità". L'algoritmo visiterà e colorerà tutti i nodi dell'albero andando a partire da un colore bianco fino ad una colorazione di nero passando per quella grigia per indicare gli stati di: 
- non scoperto $\rightarrow$ bianco
- scoperto $\rightarrow$ grigio
- conclusa la visita $\rightarrow$ nero
Andrà quindi ad esplorare tutti i possibili nodi raggiungibili da quello di partenza prima di passare in primis alla colorazione di nero del nodo di partenza e in secundis al passagio al secondo nodo da cui partire
L'algoritmo farà utilizzo di uno stack per l'implementazione dell'algoritmo.
````python
def DFS(G):
    (color, predecessor) = Init(G)
     t = 0
     for each v in V:
        if color(v) == bn:
            (color, predecessor, discovery, finish, time) = DFS_Visit(G, v, color, predecessor, discovery, finish, time)
    return (color, predecessor, discovery, finish)

def DFS_Visit(G, v, color, predecessor, discovery, finish, time)
    color(v) = gr
    discovery(v) = time
    time++

    for each w in Adj(v):
        if color(w) = bn:
            predecessor(w) = v
            (color, predecessor, discovery, finish, time) = DFS_Visit(G, w, color, predecessor, discovery, finish, time)
    color(v) = nr 
    finish(v) = t
    t++
    return (color, predecessor, discovery, finish, time)
```
