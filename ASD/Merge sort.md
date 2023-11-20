---
author: Lorenzo Tecchia
tags:
  - algorithm/sort
  - to-do/implementation
---
>[!todo] 
>- [ ] Implementazione in C

## [[Algoritmo]]

```python 
def algorithmMergeSort(A, n):
	MergeSort(A, 0, n-1)
```

```python
def MergeSort(A, p, r):
	if p < r:
		q = ((p + r) / 2)
		MergeSort(A, p, q)
		MergeSort(A, q + 1, r)
		Merge(A, p, q, r)
```

Tramite il concetto di [[dividi et impera]] le due chiamate ricorsive, dividono la sequenza a metà.

Il caso base è $p<r$,dove $p$ è l'indice di inizio del vettore, $r$ è quello della fine. Se $p > r$ allora il vettore non è più divisibile.

```python
def Merge(A, p, q, r):
	L = Copy(A, p, q)      # Copia nell'array L, l'intervallo [p,q] di A
	R = Copy(A, q + 1, r)  # Copia nell'array R, l'intervallo [q+1,r] di A
	i, j = 0
	for k = p in range(r):
		if (i <= q - p) and ((j <= r - q) or (L[i] <= R[j])):
			A[k] = L[i]
			i++
		else
			A[k] = R[i]
			j++
```

$i \leq q-p$ controlla se l'array $L$ è finito. Infatti la dimensione di $L$ è proprio $q-p$. 
- Nel caso in cui $i>q-p$, l'$if$ sarà falso, dunque entrerà sempre nell'$else$; ovvero inserisce i rimanenti elementi d $R$.
- Altrimenti controlla lo stesso per il sotto-vettore $R$ con $j \leq r-q$
#### Analisi
![[appuntiIngenito.pdf#page=13]]

---
## Implementazione in C
```C
```