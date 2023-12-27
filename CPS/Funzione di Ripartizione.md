---
tags:
  - definition
  - probability
  - distribution
author: Lorenzo Tecchia
aliases:
  - ripartizione
---
La **funzione di [[distribuzione]]** (o di ripartizione) $F$ di una [[variabile aleatoria]] $X$, è definita, per ogni numero reale $x$, tramite $$F(x):= \mathbb{P}(X \leq x)$$.

Quindi $F(x)$ esprime la [[probabilità]] che la [[variabile aleatoria]] $X$ assuma un valore minore o uguale a $x$. 

Useremo la notazione $F_{X}$ per indicare che $F$ è la funzione di [[distribuzione]] di $X$. Tutte le questioni che si possono sollevare su una [[variabile aleatoria]], ammettono una risposta in termini della sua funzione di ripartizione.  

---
### Proprietà caratteristiche di una funzione di ripartizione
1. Siano $X$ una variabile aleatoria, $F$ la sua funzione di ripartizione. Valgono le seguenti proprietà:
	1. $0 \leq F(t) \leq 1, \qquad \forall t \in \mathbb{R};$
	2. $F$ è non decrescente, cioè, per ogni coppia $x, y$ di numeri reali, con $x \leq y$ risulta $$F(x) \leq F(y);$$
	3. Valgono le relazioni $$\lim _{t \rightarrow-\infty} F(t)=0 ; \quad \lim _{t \rightarrow+\infty} F(t)=1$$
	4. $F$ è continua a destra, cioè per ogni $x \in \mathbb{R}$ si ha $$F\left(x^{+}\right):=\lim _{t \rightarrow x^{+}} F(t)=F(x)$$
	
>[!note]
> Per quanto evidente, si sottolinea il fatto che con la scrittura $F(x^{+})$ non si intende il valore di $F$ nel punto (inesistente!) $x^{+}$, ma il limite da destra verso $x$

2. Viceversa, sia $F:\mathbb{R} \mapsto \mathbb{R}$ una funzione, che gode di tutte le proprietà (1.1), (1.2), (1.3), (1.4) elencate sopra. Allora esiste una variabile aleatoria $X$, definita su un opportuno spazio di probabilità, che ammette $F$ come sua funzione di ripartizione. 

