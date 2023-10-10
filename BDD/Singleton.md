---
author: Simone Parente
---
# Singleton

>[!hint] Il design pattern ***Singleton*** si assicura che ci sia un’**unica istanza di una classe** e **garantisce accesso globale** a quest’ultima.

### Motivazione

- In alcune situazioni è importante garantire l’esistenza di un’********unica******** istanza di una classe., soprattutto in casi in cui averne più di una porterebbe problemi di stabilità al sistema.

Possiamo avere diverse stampanti connesse alla stessa rete, ma la ***coda di stampa*** dovrà essere **unica**.

---
### Soluzione
Possiamo fare in modo che sia la classe stessa a creare quell’istanza, in modo tale da poter controllare il numero di istanze create.

-----
### Implementazione
Definire un metodo `getInstance()` all’interno della classe , questo metodo consentirà ai client di accedere all’unica istanza esistente della classe. Il suddetto può anche essere il responsabile della creazione della sua unica istanza.

Una classe di tipo Singleton deve:

- Assicurarsi che una classe abbia un’unica istanza
- Essere accessibile globalmente.
- `instance` sia di tipo static.

```java
public static ConnessioneDB getInstance() throws SQLException {
        if (instance == null) { //se non esiste ancora un'istanza allocata
            instance = new ConnessioneDB(); //alloco l'istanza
        } else if (instance.connection.isClosed()) { //se la rete è "chiusa"
            instance = new ConnessioneDB(); //creiamo una nuova istanza
        }
        return instance; //infine ritorniamo l'istanza
    }
```
### Conseguenze
- L’implementazione **potrebbe essere meno efficiente di una implementazione globale**.