---
tags: [aleatoryVariable, definition, probability, to-do]
author: Lorenzo Tecchia
---
>[!todo]
> Inserire grafico

Una [[variabile aleatoria]] [[ContinuaVA|continua]] la cui funzione di densità di probabilità è data da: $$f(x) = \begin{cases} \lambda e^{-\lambda x} &se \ x \geq 0\\
0 & se \ x < 0
\end{cases}$$
per un opportuno valore della costante $\lambda > 0$, si dice esponenziale con parametro (*o densità*) $\lambda$.

La [[funzione di distribuzione]] di una tale variabile aleatoria è data da:$$\begin{align}
\mathcal{F}(x) &= \mathbb{P}(X \leq x) \\
&= \int_{0}^{x}\lambda e^{-\lambda y}dy \\
&= 1 - e^{- \lambda x}, \;\;\;\;\; x \geq 0
\end{align}$$
Nella pratica, la distribuzione esponenziale può rappresentare il tempo di attesa prima che si verifichi un certo evento causale. Come per esempio:
>[!example]
> Il tempo che trascorrerà (a partire da questo momento), fino al verificarsi, di un terremoto; o allo scoppiare di un nuovo conflitto, o al giungere della prossima telefonata di qualcuno che ha sbagliato numero.

Sono tutte variabili aleatorie che in pratica tendono ad avere distribuzioni esponenziali.

La proprietà centrale della distribuzione esponenziale è la sua assenza di *memoria*. Con questa espressione, riferita ad una variabile aleatoria positiva $X$ si s intende che:$$\mathbb{P}(X > s + t|X > t) =\mathbb{P}(X> s)\;\;\;\;\;\;\forall s,t \geq 0$$