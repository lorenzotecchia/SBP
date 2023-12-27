---
tags:
  - probability
  - definition
  - aleatoryVariable
author: Lorenzo Tecchia
---
Le **variabili aleatorie** sono quantità di interesse  che sono determinate dal risultato di un esperimento casuale. Siccome il valore di una variabile aleatoria è determinato dall'esito dell'esperimento, possiamo assegnare delle probabilità ai suoi valori possibili.

>[!tip] ## Definzione
> Sia $(\varOmega, \mathcal{A}, P)$ uno spazio di probabilità. Una ***variabile aleatoria*** è una funzione $X: \varOmega \mapsto \mathbb{R}$ tale che, per ogni $t \in \mathbb{R}$ risulti $X \leq t \in \mathcal{A}$.
> > [!note]
> >  La precedente definizione è giustificata dal fatto che, affinché tutti i sottoinsiemi del tipo $\{X \in I\}$, con $I$ insieme misurabile, siano eventi, è necessario e sufficiente supporre che lo siano i sottoinsiemi $\{X \leq y\}$ (cioè quelli per i quali $I$ è una semiretta sinistra chiusa del tipo $(-\infty, y]$). La cosa è di semplice verifica ad esempio se $I$ è un intervallo $(a,b]$. Più delicata è la dimostrazione per gli intervalli ridotti ad un solo punto $(I = \{x\})$. Essa fa uso della proprietà di stabilità rispetto alle intersezioni numerabili della $\sigma-$algebra $\mathcal{A}$, e non sarà svolta in questa sede.

