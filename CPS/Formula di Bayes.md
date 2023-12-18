---
author: Lorenzo Tecchia
tags:
  - definition
  - probability
  - example
---
>[!example]
> Una segnale proviene il $40\%$ delle volte da un'apparecchiatura $A_{1}$ e per il restante $60\%$ delle volte da una seconda apparecchiatura $A_{2}$. Esso può essere di due tipi: "lungo" (_L_) oppure "breve" (_B_).
> È noto che $A_{1}$ (rispettivamente $A_{2}$) trasmette un segnale di tipo _L_ il $52\%$ (rispettivamente $37\%$) delle volte. In un certo istante viene ricevuto un segnale di tipo $B$; qual è la [[probabilità]] che esso provenga da $A_{1}$?
> Consideriamo gli eventi 
> $$
\begin{gathered}
A_1=\left\{\text { il segnale proviene da } A_1\right\} ; \\
A_2=\left\{\text { il segnale proviene da } A_2\right\} ; \\
L=\{\text { il segnale risulta } L\} ; \\
B=\{\text { il segnale risulta } B\}
\end{gathered}
> $$
> Le informazioni in nostro possesso possono essere formalizzate come segue:
> $$
P\left(A_{1}\right)=0.4 ; \quad P\left(A_{2}\right)=0.6 ; \quad P\left(L \mid A_{1}\right)=0.52 ; \quad P\left(L \mid A_{2}\right)=0.37
>$$
>Di conseguenza si ha anche:
> $$
P\left(B \mid A_{1}\right)=1-P\left(L \mid A_{1}\right)=0.48 ; \quad P\left(B \mid A_{2}\right)=1-P\left(L \mid A_{2}\right)=0.63 .
> $$
> L'esercizio chiede la probabilità condizionale $P(A_{1}|B)$. Il metodo che useremo per il calcolo sarà poi generalizzato per ottenere una formula molto importante (soprattutto in statistica), detta ***formula di Bayes***.
> Per definizione si ha
> $$
P\left(A_{1} \mid B\right)=\frac{P\left(A_{1} \cap B\right)}{P(B)}
>$$
>Calcoleremo allora il numeratore e il denominatore della frazione precedente. Cominciamo dal calcolo di $P(A \cap B)$. Si può scrivere, ancora utilizzando (in senso inverso!) la definizione di probabilità condizionale
> $$
P\left(A_{1} \cap B\right)=P\left(B \mid A_{1}\right) P\left(A_{1}\right)=0.48 \times 0.4=0.192 .
>$$
> Possiamo ora al calcolo di $P(B)$. Si può scrivere 
> $$
B=B \cap \Omega=B \cap\left(A_{1} \cup A_{2}\right)=\left(B \cap A_{1}\right) \cup\left(B \cap A_{2}\right) \text {; }
>$$
> dato che $A_{1}$ e $A_{2}$ sono due eventi tra loro disgiunti, anche gli eventi $B \cap A_{1}$ e $B \cap A_{2}$ lo saranno, dunque, per la proprietà additiva della probabilità, avremo 
> $$
P(B)=P\left(B \cap A_{1}\right)+P\left(B \cap A_{2}\right) .
>$$
>$P(B \cap A_1)$ è gia stata calcolata sopra e vale $0.192$. Nello stesso modo si ha 
>$$
P\left(A_{2} \cap B\right)=P\left(B \mid A_{2}\right) P\left(A_{2}\right)=0.63 \times 0.6=0.378 .
>$$
>Si conclude allora che 
>$$
P(B)=0.192+0.378=0.57,
>$$
>ed infine
> $$
P\left(A_{1} \mid B\right)=\frac{P\left(A_{1} \cap B\right)}{P(B)}=\frac{0.192}{0.57}=0.3368
>$$
>Avendo in mente l'esercizio appena svolto, passiamo enunciare e dimostrare la _formula di Bayes_, di cui esso non è che un'applicazione.

>[!tip] Definizione
> Siano $(\varOmega, \mathcal{A}, P)$ uno [[spazio di probabilità]]  fissato, e $A_{1}, \dots, A_{n}\; n$ eventi in $\mathcal{A}$. Si dice che $A_{1}, \dots, A_{n}$ è una partizione di  $(\varOmega, \mathcal{A}, P)$ se valgono entrambe le seguenti proprietà:
> 1. $\bigcup_{i=1}^{n}A_{i}=\varOmega$
> 2. $A_{i}\cap A_{j}= \emptyset \qquad \forall(i,j) \;\text{con}\; i \neq j$
> > [!note] Osservazione 
> > Gli eventi di una partizione vanno pensati come una famiglia di $n$ eventualità che possono prodursi durante lo svolgersi dell'esperimento; esse esauriscono tutte le possibilità (sicuramente una di esse si verifica)   e si escludono a vicenda (due di esse non possono verificarsi contemporaneamente). Nell'esercizio iniziale, ad esempio si trattava di $A_{1}$ e $A_{2}$: il segnale proviene sicuramente da una delle due apparecchiature, na non da tutte e due contemporaneamente.


### Formula di Bayes
Sia $(\varOmega, \mathcal{A}, P)$ uno spazio di probabilità. Sia $A_{1}, \dots, A_{n}$ una partizione di $\varOmega$, tale che $P(A_{i}) > 0$per ogni $i=1, \dots, n$. Sia infine $B$ un [[evento]] con $P(B) > 0$. Allora per ogni $k = 1, \dots, n$ risulta
$$
P\left(A_{k} \mid B\right)=\frac{P\left(B \mid A_{k}\right) P\left(A_{k}\right)}{\sum_{i=1}^{n} P\left(B \mid A_{i}\right) P\left(A_{i}\right)}
$$
^formula-Bayes


>[!note]
> La [[Formula di Bayes#^formula-Bayes|formula di Bayes]] è nota con il nome di formula delle _probabilità delle cause_: interpretando gli eventi della [[Funzione di Ripartizione|ripartizione]] come $n$ possibili "cause" per il verificarsi di $B$, la formula permette il calcolo della probabilità che, sapendo che $B$ si è verificato, la causa sia stata $A_{k}$. Per questo motivo viene spesso usato per calcolare le probabilità cosiddette a _posteriori_: per esempio, avendo determinati sintomi di un paziente, si può utilizzare la formula per verificare la correttezza della diagnosi proposta.


Dimostrazione (del teorema). Come nell'esercizio, risulta


$$
P\left(A_{k} \cap B\right)=P\left(B \mid A_{k}\right) P\left(A_{k}\right)
$$
^formula-176

Inoltre si può scrivere

$$
B=B \cap \Omega=B \cap\left(\cup_{i=1}^{n} A_{i}\right)=\cup_{i=1}^{n}\left(B \cap A_{i}\right)
$$

Poiché gli eventi ( $B \cap A_{i}$ ) sono tra loro due a due disgiunti (perché?), per l'assioma di addittività della probabilità si ottiene
$$
P(B)=\sum_{i=1}^{n} P\left(B \cap A_{i}\right)
$$
^formula-177

La formula [[Formula di Bayes#^formula-177|(1.7.7)]] va sotto il nome di formula della partizione dell'evento certo; ad essa abbiamo accennato all'inizio del paragrafo 1.3. Essa può essere utilizzata per calcolare la probabilità di $B$ quando si sappia calcolare ciascuna delle probabilità che $B$ si verifichi contemporaneamente ad una delle eventualità $A_{i}$ (cioè che si verifichi l'evento $B \cap A_{i}$ ).

Come abbiamo fatto in precedenza (formula [[Formula di Bayes#^formula-176|(1.7.6)]]) si può scrivere
$$
P\left(A_{i} \cap B\right)=P\left(B \mid A_{i}\right) P\left(A_{i}\right),
$$
e quindi la [[Formula di Bayes#^formula-177|(1.7.7)]] diventa
$$
P(B)=\sum_{i=1}^{n} P\left(B \mid A_{i}\right) P\left(A_{i}\right)
$$
^formula-178

Dalle formule [[Formula di Bayes#^formula-176|(1.7.6)]] e [[Formula di Bayes#^formula-178|(1.7.8)]] si ricava allora
$$
P\left(A_{k} \mid B\right)=\frac{P\left(A_{k} \cap B\right)}{P(B)}=\frac{P\left(B \mid A_{k}\right) P\left(A_{k}\right)}{\sum_{i=1}^{n} P\left(B \mid A_{i}\right) P\left(A_{i}\right)}
$$

ovvero la formula di Bayes che cercavamo.
>[!example]
> Una particolare analisi del sangue è efficace al $99\%$ nell'individuare una certa malattia quando essa è presente. Si possono però anche verificare dei "falsi positivi" con probabilità dell $1\%$(ovvero una persona sana che si sottoponga al test, con una probabilità di $0.01$ risulta erroneamente affetta dalla malattia in questione). Se l'incidenza cdi questo male sulla [[popolazione]] è dello $0.5\%$, qual è la probabilità che un soggetto sia malato, condizionata al fatto che le analisi abbiano dato [[esito]] positivo?
> Sia $M$ l'evento "il soggetto è malato" ed $E$ l'evento "il risultato dell'analisi è positivo". Allora $\mathbb{P}(M|E)$ si trova tramite:$$ \begin{align}
\mathbb{P}(M|E) &= \frac{\mathbb{P}(M \cap E)}{\mathbb{P}(E)} \\
&= \frac{\mathbb{P}(E|M)\mathbb{P}(M)}{\mathbb{P}(E|M)\mathbb{P}(M)+\mathbb{P}(E|M^{c})\mathbb{P}(M^{c})} \\
&= \frac{0.99 \times 0.005}{0.99 \times 0.005 + 0.01 \times 0.995} \approx 0.3322
\end{align}$$
Perciò solo il $33\%$ delle persone che risultano positive alle analisi sono realmente affette dalla malattia. Siccome molti studenti si stupiscono di questo risultato (infatti le caratteristiche del test sembrano buone e ci si aspetterebbe un valore più elevato), vale forse la pena di presentare una seconda argomentazione che anche se meno rigorosa può aiutare a chiarirsi le idee.
Se lo $0.5\% = 1/200$ della [[popolazione]] soffre di questo male, in [[Valore atteso|media]] su $200$ persone vi sarà un solo malato. Se egli si sottopone alle analisi, verrà trovato positivo quasi certamente con (probabilità $0.99$), così che su $200$ individui testati ve ne saranno in [[Valore atteso|media]] $0.99$ che saranno correttamente individuati come malati. D'altro canto le (in media) 199 persone sane che hanno una probabilità di $0.01$ di risultare positive, e quindi in media su $200$ analisi vi saranno $199 \times 0.01 = 1.99$ falsi positivi. Se consideriamo che ogni $0.99$ positivi veri vi sono in media $1.99$ positivi falsi, ricaviamo nuovamente che la frazione di malati reali tra i soggetti positivi alle analisi è$$\frac{0.99}{0.99 + 1.99} \approx 0.3322$$

>[!note] 
> L'[[Formula di Bayes#^formula-di-bayes|equazione della formula di Bayes]] è utile anche quando si voglia riconsiderare il proprio (personale) convincimento o confidenza su un fatto, alla luce di nuove informazioni.
