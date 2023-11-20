---
author: Lorenzo Tecchia
tags:
  - algorithm/sort
  - to-do/implementation
---
>[!todo] 
>- [ ] Implementazione in C

Insertion sort è un [[algoritmo]]  di [[ordinamento]] abbastanza efficiente per l'ordinamento di array di piccole dimensioni.
#### Pseudo codice
###### Algoritmo Ricorsivo
```python
def InsertionSort(A, n):
	if n > 1:
		InsertionSort(A, n-1)
		Insert(A, n-1)
```
###### Algoritmo Iterativo
```python
def InsertionSort(A, n):
	for i = 1 in range(n-1):
		Insert(A, i)
```

```python
def Insert(A, i):
	x = A[i]
	j = i - 1
	while (j >= 0 and A[j] > x):
		A[j+1] = A[j]
		j--
	A[j+1] = x
```
---
#### Correttezza
---
#### [[Analisi asintotica|Analisi]] dell'algoritmo iterativo
$$\sum^{n}_{i=1}T_{insert}(A,i) = \sum^{n}_{i=1}\Theta (k^{A}_{i}) = \Theta(\sum^{n}_{i=1}k^{A}_{i})$$
- Se $k^{A}_{i} = i$ (_caso peggiore_)
	$$\sum^{n}_{i=1}i = \frac{n(n+1)}{2} \rightarrow \Theta(n^{2})$$
	`Esempio: 10 9 8 7 6 5 4 3 2 1 0`

- Se $k^{A}_{i} = 1$ (_caso migliore_)
	$$\sum^{n}_{i=1}1 = n \rightarrow \Theta(n)$$
	`Esempio: 0 1 2 3 4 5 6 7 8 9 10`
#### [[Analisi asintotica|Analisi]] dell'algoritmo ricorsivo
![[appuntiIngenito.pdf#page=13]]

---
## Implementazione in C
```C
// da implementare
```