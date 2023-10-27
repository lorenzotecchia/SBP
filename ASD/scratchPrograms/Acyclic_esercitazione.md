---
tags: [exercise, example]
author: Lorenzo Tecchia
---
# Esercitazione sull'algoritmo della aciclicità di un grafo
```python
def Acyclic(G):
    color = Init(G)
    for each v in V:
        if c(v) == bn:
            acyclic = DFSAcyclic(G, v)
            if !acyclic:
                return False
    return True 
```


```python
def DFSAcyclic(G, v):
    c(v) = gr
    for each w in Adj[v]:
        if c(w) = bn:
            acyclic = DFSAcyclic(G,w)
            if !acyclic:
                return False
        else if c(w) = gr:
            return False
    c(v) = nr
    return True
```

