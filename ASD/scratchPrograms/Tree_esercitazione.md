---
tags: [example, exercise]
author: Lorenzo Tecchia
---
# Ricostruzione degli algoritmi di visita in post/pre/in order su alberi binari di ricerca

````python
def DFVIN(X, F, a):
    if x != NULL:
        a = DFVIN(x.sx, F, a)
        a = F(x.dato, a)
        a = DFVIN(x.dx, F, a)
    return a
```

```python
def DFVPOST(X, F, a):
    if x != NUll:
        a = DFVPOST(x.sx, F, a)
        a = DFVPOST(s.dx, F, a)
        a = F(x.dato)
    return a
```

```python
def DFVPRE(X, F, a):
    if x != NULL:
       a = F(x.dato)
       a = DFVPRE(x.sx, F, a)
       a = DFVPRE(x.dx, F, a) 
    return a
```
