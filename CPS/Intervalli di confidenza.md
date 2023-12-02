---
author: Lorenzo Tecchia
tags: [definition, aleatoryVariable, probability, statistics]
---
Sia $X_{1}, X_{2}, \dots, X_{n}$ un [[campione]] estratto da una popolazione [[Gaussiana|normale]] di [[Valore atteso|media]] incognita $\mu$ e [[varianza]] nota $\sigma^{2}$. Avviamo in precedenza dimostrato che $\overline{X} := \sum_{i}X_{i}/n$ è lo stimatore di massima verosimiglianza per $\mu$. Ciò non significa che  possiamo aspettarci che la [[Valore atteso|media]] sia esattamente uguale  $\mu$, ma solo che le sarà vicina.
Perciò, rispetto ad uno stimatore puntuale, è a volte preferibile poter produrre un intervallo per il quale abbiamo un certo livello di fiducia (confidenza), che il parametro $\mu$ vi appartenga. Per ottenere un tale ***intervallo di confidenza***, dobbiamo fare uso della [[distribuzione]] di [[probabilità]] dello stimatore puntuale. 

Ricordiamo intanto che nelle ipotesi in cui ci siamo messi, $\overline{X}$ è [[Gaussiana|normale]] di media $\mu$ e varianza $\sigma^{2}/n$. Ne segue che $$\frac{\bar{X}-\mu}{\sigma / \sqrt{n}} \sim \mathcal{N}(0,1)$$
Perciò $$\mathbb{P}\left(-1.96<\frac{\bar{X}-\mu}{\sigma / \sqrt{n}}<1.96\right) \approx 0.95$$ o equivalentemente,
$$
\mathbb{P}\left(-1.96 \frac{\sigma}{\sqrt{n}}<\bar{X}-\mu<1.96 \frac{\sigma}{\sqrt{n}}\right) \approx 0.95
$$
da cui, moltiplicando le disuguaglianza per $-1$, 
$$
\mathbb{P}\left(1.96 \frac{\sigma}{\sqrt{n}}>\mu-\bar{X}>\ddot{-1.96} \frac{\sigma}{\sqrt{n}}\right) \approx 0.95$$
ovvero, finalmente, 
$$
\mathbb{P}\left(\bar{X}-1.96 \frac{\sigma}{\sqrt{n}}<\mu<\bar{X}+1.96 \frac{\sigma}{\sqrt{n}}\right) \approx 0.95$$

Il $95\%$ circa delle volte $\mu$ starà ad una distanza non superiore a $1.96\sigma/\sqrt{n}$ dalla [[media aritmetica]] dei dati. Se osserviamo il campione, e registriamo che $\overline{X} = \bar{x}$ allora possiamo dire che "con il $95\%$ di confidenza" $$\bar{x}-1.96 \frac{\sigma}{\sqrt{n}}<\mu<\bar{x}+1.96 \frac{\sigma}{\sqrt{n}}$$ 
Stiamo quindi affermando che, con il $95\%$ di confidenza, la media vera della distribuzione appartiene all'intervallo $$\left(\bar{x}-1.96 \frac{\sigma}{\sqrt{n}}, \quad \bar{x}+1.96 \frac{\sigma}{\sqrt{n}}\right)$$
>[!important] Questo intervallo è detto ***intervallo di confidenza ad un livello del $95\%$***, o più semplicemente ***intervallo di confidenza al $95\%$*** per $\mu$

>[!example]-
> Supponiamo che quando un segnale elettrico di valore $\mu$ viene trasmesso dalla sorgente $A$, il ricevente $B$ registri un valore distribuito come una [[Gaussiana|normale]] di [[Valore atteso|media]] $\mu$ e [[varianza]] $4$. Altrimenti detto, se $\mu$ è il segnale inviato, quello ricevuto è $\mu + N$, dove $N$ denota il rumore, ed è $N \approx \mathcal{N}(0, 4)$. Immaginiamo che per riprodurre l'errore, lo stesso segnale è stato trasmesso $9$ volte. I valori registrati da $B$ in ricezione sono stati $$\begin{array}{lllllllll}5 & 8.5 & 12 & 15 & 7 & 9 & 7.5 & 6.5 & 10.5\end{array}$$
> Cerchiamo di ottenere un intervallo di confidenza al $95\%$ per $\mu$.
> Siccome $$\bar{x}=\frac{81}{9}=9$$ ne segue, sotto l'ipotesi aggiuntiva che i valori ricevuti siano indipendenti, che un intervallo di confidenza al $95\%$ per $\mu$ è $$
\left(9-1.96 \frac{2}{3}, \quad 9+1.96 \frac{2}{3}\right)=(7.69,10.31)$$
> Perciò possiamo dire di avere il "$95\%$ di fiducia" che il vero messaggio fosse compreso tra $7,69$ e $10.31$

>[!important]
> Gli intervalli di confidenza trovati fin qui sono detti in particolare *bilaterali*, perché hanno due estremi infiniti. 

Altre volte invece siamo interessati a determinare un singolo valore che ci permetta ad esempio di affermare con il $95\%$ di confidenza che $\mu$ è superiore. 
Per trovare un valore siffatto, si noti che se $Z$ e $\mathcal{N}(0, 1)$, allora $$
\begin{aligned}
0.95 & \approx P(Z<1.645) \\
& \approx P\left(\frac{\bar{X}-\mu}{\sigma / \sqrt{n}}<1.645\right) \\
& \approx P\left(\bar{X}-1.645 \frac{\sigma}{\sqrt{n}}<\mu\right)
\end{aligned}$$ così che un intervallo di confidenza unilaterale destro ad un livello del $95\%$ per $\mu$ è il seguente, $$\left(\bar{x}-1.645 \frac{\sigma}{\sqrt{n}}, \infty\right)$$ dove $\bar{x}$ è il valore che si osserva per la [[Valore atteso|media]] campionaria.

![](https://cdn.mathpix.com/cropped/2023_11_20_03d5e6ef9957032926fdg-127.jpg?height=242&width=542&top_left_y=206&top_left_x=1924)

Si possono analogamente definire anche gli intervalli di confidenza unilaterali sinistri, e ad esempio dello al $95\%$ per $\mu$ è $$\left(-\infty, \quad \bar{x}+1.645 \frac{\sigma}{\sqrt{n}}\right)$$

>[!example]- Si determino al $95\%$ di confidenza degli intervalli destro e sinistro per il parametro $\mu$ per l'esmpio precedente
> Siccome $$1.645 \frac{\sigma}{\sqrt{n}}=\frac{3.29}{3} \approx 1.097$$ l'intervallo destro al $95\%$ è $$(9-1.097, \infty)=(7.903, \infty)$$ mentre quello sinistro è $$(-\infty, 9+1.097)=(-\infty, 10.097)$$

Si possono ottenere intervalli di confidenza per ogni livello di confidenza assegnato. Si ricordi che avevamo definito i numeri $z_{\alpha}$ in modo tale che $$\mathbb{P}\left(Z>z_{\alpha}\right)=\alpha$$ dove $Z \sim \mathcal{N}(0, 1)$. Questo implica che per ogni $\alpha \in (0,1)$ $$P\left(-z_{\alpha / 2}<Z<z_{\alpha / 2}\right)=1-\alpha$$
Da questa equazione si deduce facilmente che $$
\begin{aligned}
1-\alpha & =P\left(-z_{\alpha / 2}<\frac{\bar{X}-\mu}{\sigma / \sqrt{n}}<z_{\alpha / 2}\right) \\
& =P\left(-z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}<\bar{X}-\mu<z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}\right) \\
& =P\left(z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}>\mu-\bar{X}>-z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}\right) \\
& =P\left(\bar{X}-z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}<\mu<\bar{X}+z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}\right)
\end{aligned}$$
Quindi un intervallo di confidenza bilaterale ad un livello di $1-\alpha$ per $\mu$ è $$
\left(\bar{x}-z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}, \quad \bar{x}+z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}\right)$$ dove $\bar{x}$ è il valore che si osserva per la [[Valore atteso|media]] campionaria.
In maniera del tutto analoga, dal fatto che $$Z:=\frac{\bar{X}-\mu}{\sigma / \sqrt{n}}$$ è una [[Gaussiana|normale]] standard, e dalle identità $$
\begin{array}{r}
P\left(Z>z_{\alpha}\right)=\alpha \\
P\left(Z<-z_{\alpha}\right)=\alpha
\end{array}$$ si deducono gli intervalli di confidenza unilaterali per qualunque livello di confidenza. 
In particolare si ottiene che $$
\left(\bar{x}-z_{\alpha} \frac{\sigma}{\sqrt{n}}, \infty\right) \quad \text { e } \quad\left(-\infty, \quad \bar{x}+z_{\alpha} \frac{\sigma}{\sqrt{n}}\right)$$ sono gli intervalli di confidenza unilaterali ad un livello di $1-\alpha$ per $\mu$.

---
>[!tip] ## Confidenza, non [[probabilità]]
> L'espressione "vi è un livello di confidenza del $95\%$ che $\mu$ stia nell'intervallo" può portare a interpretazioni erronee. È bene notare che *non stiamo affermando* che la probabilità che $\mu \in (\bar{x} - 1.96\sigma / \sqrt{n})$ è di $0.95$, infatti in questo enunciato non compaiono variabili aleatorie. Quello che affermiamo , invece, è che la tecnica adottata per arrivare a questo intervallo, nel $95\%$ dei casi in cui viene impiegata, produce un intervallo che contiene il valore vero di $\mu$. In altri termini, prima di osservare i dati possiamo dire che vi è il $95\%$ di probabilità che l'intervallo che otterremo contenga $\mu$, mentre dopo l'osservazione dei dati possiamo solo asserire che l'intervallo contiene $\mu$ "col $95\%$ di confidenza"