---
author: Lorenzo Tecchia
tags: [definition, statistics]
---
Siano assegnate due variabili aleatorie $X$ e $Y$ di media $\mu_{X}$ e $\mu_{Y}$ rispettivamente. La loro ***covarianza***, che si indica con $\operatorname{Cov}(X, Y)$ è (se esiste) la quantità $$
\operatorname{Cov}(X, Y):=E\left[\left(X-\mu_{X}\right)\left(Y-\mu_{Y}\right)\right]$$
Si può ottenere anche una formula alternativa più semplice, analoga a quella qui sopra, per la varianza. Si trova espandendo il prodotto al secondo membro.
$$
\begin{aligned}
\operatorname{Cov}(X, Y) & =E\left[X Y-\mu_{X} Y-\mu_{Y} X+\mu_{X} \mu_{Y}\right] \\
& =E[X Y]-\mu_{X} E[Y]-\mu_{Y} E[X]+\mu_{X} \mu_{Y} \\
& =E[X Y]-\mu_{X} \mu_{Y}-\mu_{X} \mu_{Y}+\mu_{X} \mu_{Y} \\
& =E[X Y]-E[X] E[Y]
\end{aligned}$$
Quindi si deduce la simmetria:$$\operatorname{Cov}(X, Y) = \operatorname{Cov}(Y, X)$$
così come la generalizzazione del concetto di [[varianza]] $$\operatorname{Cov}(X, X)=\operatorname{Var}(X)$$


