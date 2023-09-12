---
author: Lorenzo Tecchia
tags:
  - definition
---
Una ***ricorrenza*** è una equazione o disequazione che descrive una funzione in termini dei suoi valori su input più piccoli.

>[!important]
> Permette di descrivere i [[tempi di esecuzione]] degli algoritmi divide et impera.
## Risoluzioni
### Sostituzione
Nel ***metodo di sostituzione***, ipotizziamo un limite e poi usiamo l'induzione matematica per dimostrare che la nostra ipotesi sia corretta
#### Esempio
### Albero delle ricorrenze
Il ***metodo dell'albero delle ricorrenze o albero di [[ricorsione]]*** converte la ricorrenza in un albero i cui nodi rappresentano i costi ai vari livelli della ricorsione; per risolvere la ricorrenza, adotteremo delle tecniche che limitano le sommatorie.
>[!tip] 
> Di solito, in questo caso, è buona norma andare a disegnare l'albero delle ricorrenze fino ad un livello che ci permetta di interpretare l'andamento
#### Esempio
### Metodo dell'esperto
Il ***metodo dell'esperto*** fornisce i limiti per ricorrenze nella forma $$T(n)=a\;T(n/b)+f(n)$$
dove $a\geq 1, b > 1$ e $f(n)$ è una funzione data.
#### Esempio
