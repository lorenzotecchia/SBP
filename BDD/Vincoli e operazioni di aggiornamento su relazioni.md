---
Date: September 30, 2022
Number: 6
Reviewed: Yes
Status: Done
author: Simone Parente Martone
---
## Inserimento
Una Insert potrebbe violare tutti e quattro i tipi di vincoli
### Dominio
Se un valore di un attributo non appare nel corrispettivo dominio
### Chiave
Se il valore della chiave nella nuova tupla già esiste nella relazione.
### Integrità di entità
Se la chiave primaria è inserita come `NULL`.
### Integrità referenziale
Il valore di una chiave esterna riferisce ad una tupla che non esiste nella relazione referenziata.
### Gestione della violazione
1. forzare l’inserimento completo (della relazione riferita)
2. rifiutare l’inserimento
Nel primo caso, l’inserimento potrebbe andare ad impattare a cascata l’inserimento su altre relazioni
## Cancellazione
Può violare solo il vincolo di integrità referenziale, per la gestione possiamo:
- rigettare la cancellazione
- tentare di propagare la cancellazione (cancella fino ad un punto indefinito)
- modificare i valori dell’attributo referenziante (posto a null)
- Combinare le 3 precedenti (il DBMS dovrebbe permettere all’user di specificare la gestione)