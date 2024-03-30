## 2024-01-17
Si scriva un algoritmo ricorsivo che, dati in ingresso un albero binario $T$ contenente numeri interi e due numeri naturali $l_{1} \leq l_{2}$, restituisca la somma dei valori $d$ di tutti quei nodi con $d$ pari e la cui profondità $p$ non sia compresa tra $l_{1}$ e $l_{2}$. Tale algoritmo dovrà essere efficiente e non far uso né di variabili globali, né di di parametri passati per riferimento. Si scriva infine un algoritmo iterativo che simuli precisamente l'algoritmo ricorsivo di cui sopra.

### Esecuzione
```python
def Algo(T, l1, l2):
	if T != NULL:
		s = Algo(T -> sx, l1 --, l2--)
		s = s + Algo(T -> dx, l1--, l2--)
		if l1 >= 0 && l2 <= 0 && T -> key % 2 == 0:
			s = s + T -> key
		return s
```

## 2023-03-17
 Si scriva un algoritmo ricorsivo che, presi in ingresso un albero binario $T$ contenente dati interi e un intero positivo $k$, restituisca il valore della massima profondità dei nodi con valore di chiave multiplo di $k$. Nel caso l'insieme di tali nodi fosse vuoto, è richiesta la restituzione del valore di default $-1$. L'algoritmo dovrà essere efficiente e non far uso né di variabili globali né di parametri passati per riferimento. Infine, si scriva un algoritmo iterativo che simuli precisamente l'algoritmo ricorsivo di cui sopra.

#### Esecuzione 
```python
def Algo(T, k):
    if T!= NULL:
        l = Algo(T -> sx, k)
        r = Algo(T -> dx, k)
        max = MAX{l, r}
        if max == -1:
            if T -> key % k == 0:
                return 0
            return -1
        else:
            return max + 1
    else
        return -1
```

## 2022-10-19
Si scriva un algoritmo ricorsivo che, dati in ingresso un albero binario di ricerca $T$ e un intero positivo $k$, cancelli da $T$ tutti i nodi che si trovano in posizioni multiple di $k$ nell'ordinamento totale delle chiavi dell'albero. Tale algoritmo dovrà essere efficiente e non far uso né di variabili globali né di parametri passati per riferimento. Infine, si scriva un algoritmo iterativo che simuli precisamente l' algoritmo ricorsivo di cui sopra.

#### Esecuzione
```python
def Algo(T, k, P, visited):
	if T == NULL:
		return visited
	else:
		pos = 1 + Algo(T -> sx, k, T, visited)
		visited = Algo(T -> dx, k , T, pos)
		if pos % k == 0:
			if P -> sx == T:
				P -> sx = RimuoviNodo(T)
			else:
				P -> dx = RimuoviNodo(T)
		return visited
```

## 2022-07-21
Si scriva un algoritmo ricorsivo che, dati in ingresso un albero binario di ricerca su interi $T$ e due valori $k_{1}, k_{2} \in N$, cancelli da $T$ le chiavi $k$ comprese tra $k_{1}$ e $k_{2}$ $(k_{1}\leq k \leq k_{2})$. Tale algoritmo dovrà essere efficiente e non far uso né di variabili globali né di parametri passati per riferimento. Infine, si scriva un algoritmo iterativo che simuli precisamente l'algoritmo ricorsivo di cui sopra.

#### Esecuzione 
```python
def Algo(T , k1, k2):
	if T == NULL:
		return NULL
	else:
		T -> sx = Algo(T -> sx, k1, k2)
		T -> dx = Algo(T -> dx, k1, k2)
		if T -> key \in [k1, k2]:
			T = RimuoviNodo(T)
		return T
```

## 2022-06-21
Si scriva un algoritmo ricorsivo che, dati in ingresso un albero binario di ricerca su interi $T$ e due valori $k_1, k_{2} \in N$, inserisca ni una lista $\mathcal{L}$  chiavi $k$ contenute in $T$ comprese tra $k_{1}$ e $k_{2} ( k_{1} \leq k ≤ k_{2})$ , in modo che al termine $\mathcal{L}$ contenga valori ordinati in modo decrescente. Tale algoritmo dovrà avere complessità lineare nella dimensione dell'albero. Infine, si scriva un algoritmo iterativo che simuli precisamente l'algoritmo ricorsivo di cui sopra.

#### Esecuzione
```python
def Algo(T , k1, k2, L):
    if T != NULL:
        L = Algo(T -> sx, k1, k2, L)
        if T -> key >= k1 && T -> key <= k2:
            L = InserisciInTesta(T -> key, L)
        L = Algo(T -> dx, k1, k2, L)
    return L
```