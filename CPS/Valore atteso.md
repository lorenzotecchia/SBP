---
tags: [definition, aleatoryVariable, statistics]
alias: [aspettazione]
author: Lorenzo Tecchia
---
>[!definition]
> Sia $X$ una [[variabile aleatoria]] discreta che può assumere i valori $x_{1},x_{2}, \dots$; il **valore atteso** di $X$, che si indica con $E[X]$, è (se esiste[^1]) il numero:$$E[X] := \sum\limits_{i}x_{i}\mathbb{P}(X = x_{i})$$

In altri termini si tratta della media pesata dei valori possibili di $X$, usando come pesi le [[probabilità]] che tali valori vengano assunti da $X$. Per questo $E[X]$ è anche detta media di $X$, oppure **aspettazione**.

>[!example] Per illustrare il concetto di media pesata, facciamo un semplice esempio.
> Se $X$ è una variabile aleatoria con [[funzione]] di massa: $$p(0) = \frac{1}{2}= p(1)$$ allora
> $$E[X] = 0 \times \frac{1}{2}+ 1 \times \frac{1}{2}= \frac{0+1}{2}=\frac{1}{2}$$
> é semplicemente la media aritmetica dei valori che $X$ può assumere. Però, se$$p(0) = \frac{1}{3}, \quad p(1) = 2/3$$ allora
> $$E[X] = 0 \times \frac{1}{3}+1 \times \frac{2}{3}=\frac{0+1\times2}{3}= \frac{2}{3}$$
> è una media pesata degli stessi valori $0$ e $1$, dove al secondo è stato dato un peso che è il doppio di quello del primo.

[^1]:Il valore atteso di $X$ è definito solo se la serie converge in valore assoluto, ovvero deve valere:$$\sum\limits_{i}^{X}|x_{i}|\mathbb{P}(X = x_{i})< \infty$$ In caso contrario si dice che $X$ non ha valore atteso.

---
>[!example] Sia $X$ il punteggio che si ottiene lanciando un dado non truccato, quanto vale $E[X]$?
> Siccome $\mathcal{p}(1)=\mathcal{p}(2)=\mathcal{p}(3)=\mathcal{p}(4)=\mathcal{p}(5) = \mathcal{p}(6)=\frac{1}{6}$, ricaviamo che $$
E[X]:=1 \cdot \frac{1}{6}+2 \cdot \frac{1}{6}+3 \cdot \frac{1}{6}+4 \cdot \frac{1}{6}+5 \cdot \frac{1}{6}+6 \cdot \frac{1}{6}=\frac{7}{2}=3.5$$^esempio-valoreAtteso-dadoOnesto

>[!note] 
> Il valore atteso di $X$ non è uno dei valori che $X$ può assumere. Perciò anche se $E[X]$ è chiamato ***valore atteso*** di $X$, non vuole affatto dire che noi ci attendiamo di vedere questo valore, ma piuttosto che ci aspettiamo che sia il limite a cui tende il punteggio medio del dado su un numero crescente di ripetizioni


>[!example] Valore atteso della funzione indicatrice di un [[evento]] $A$
> Sia definita tale funzione $I$ in questo modo: $$
I:= \begin{cases}1 & \text { se } A \text { si verifica } \\ 0 & \text { se } A \text { non si verifica }\end{cases}$$
> allora $$E[I]:=1 \cdot P(I=1)+0 \cdot P(I=0)=P(I=1)=P(A)$$
> Quindi il valore atteso della funzione indicatrice di un evento è la possibilità di quest'utlimo.

---
# Proprietà del valore atteso
Se anziché voler calcolare il valore atteso di $X$, interessasse determinare quello di una sua qualche funzione $g(X)$, come potremmo fare?
