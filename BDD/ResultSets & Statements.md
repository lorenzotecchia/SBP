---
author: Simone Parente
---
- Indice

# `ResultSet`

---

Classe che contiene il risultato di una query SQL ed è il punto di connessione tra le tabelle di un database e le applicazioni Java. Un ResultSet può rappresentare:

- Una tabella
- Parte di una tabella

Dispone di metodi per accedere righe e colonne rappresentate nell’oggetto e un Resultset può essere:

- **Forward only** (accesso sequenziale alle righe).
- **Scrollable** (accesso casuale).

Ogni interfaccia Resultset incapsula un operatore cursore.

## Creare un `ResultSet`

---

Gli oggetti `ResultSet` sono costruiti a partire da oggetti `Statement`, `PreparedStatement` e `CallableStatement`

Di default gli oggetti ResultSet sono di tipo *forward only* e non sono modificabili.

Questo implica che una volta visualizzate le righe di un `ResultSet` non è più possibile accedervi a meno di non rieseguire la query e creare un diverso `ResultSet`.

- Esempi
    1. Dopo aver creato un object `Statement` è possibile creare un `ResultSet` con il metodo `executeQuery`.
    
    ```java
    Connection con = ConnessioneDB.getInstance();
    Statement st = con.createStatement();
    Resultset rs = st.executeQuery(“SELECT * FROM articolo “ +
    																	 “WHERE prezzo<50”);
    while(rs.next()) {
    	System.out.println(“Codice = “ + rs.getString(“codice”)); 
    	System.out.println(“Descrizione = “ + rs.getString(“descrizione”)); 
    	System.out.println(“Prezzo = “ + rs.getString(“prezzo”));
    }
    ```
    
    1. È possibile fare lo stesso con un object di tipo `PreparedStatement`
    
    ```java
    Connection con = ConnessioneDB.getInstance();
    PreparedStatement pst =  con.prepareStatement(“SELECT * FROM articolo “ + “WHERE prezzo<50”);
    Resultset rs = pst.executeQuery();
    while(rs.next()) {
    	System.out.println(“Codice = “ + rs.getString(“codice”)); 
    	System.out.println(“Descrizione = “ + rs.getString(“descrizione”)); 
    	System.out.println(“Prezzo = “ + rs.getString(“prezzo”));
    	}
    ```
    

Un cursore possiamo vederlo come un puntatore alla riga corrente nel `ResultSet`.

Il metodo `.next()` restituisce `true` fino a quando il cursore punta a una riga valida e restituisce `false` (e provoca una `SQLException`) appena il cursore punta alla riga successiva all’ultima (oppure se il cursore si trova sopra la prima riga).


## Navigazione nel `ResultSet`

---

Se vogliamo `ResultSet` scrollabili è necessario che lo statement di partenza lo sappia

```java
Statement st = con.createStatement (ResultSet.TYPE_SCROLL_SENSITIVE, ResultSet.CONCUR_UPDATABLE);
```

- `boolean .next()`
    
    Muove il cursore alla riga successiva
    
- `boolean .previous()`
    
    Muove il cursore alla riga precedente
    
- `boolean .first()`
    
    Muove il cursore alla prima riga
    
- `boolean .last()`
    
    Muove il cursore all’ultima riga
    

- `boolean absolute(int n)` con $n \neq 0$
    - Se $n>0$ il puntatore punterà alla n-esima riga (a partire dalla prima)
    - Se $n<0$ si sposterà n righe indietro
    
    Se si raggiunge l’inizio o la fine restituisce false
    
- `boolean relative(int n)`
    - Se $n > 0$ il cursore si sposterà di n righe avanti rispetto a quella attuale
    - Se $n < 0$ il cursore si sposterà di n righe indietro rispetto a quella attuale
    - $n=0$ è consentito ma praticamente inutile

## Metodi `.getXXX`

---

Dove `XXX` indica uno dei tipi base di Java, avremo quindi i metodi:

`getString(int columnIndex);`

`getString(String columnName);`

`getInt(int columnIndex);`

`getInt(String columnName);`

`getFloat(int columnIndex);`

`getFloat(String columnName);`

`getDouble(int columnIndex);`

`getDouble(String columnName);`

eccetera…

Il primo metodo prende come parametro l’indice di una colonna, il secondo prende il nome della colonna, quindi:

`.getInt(1)` è equivalente a fare `getInt("id_articolo")`

`.getString(2)` è equivalente a fare `.getString("titolo")`

E il valore di ritorno sarà quello della riga a cui si trova il cursore del `ResultSet`.


## Tipi di Resultset

---

### ResultSet.TYPE_FORWARD_ONLY

---

Il `ResultSet` si può muovere solo in avanti con il metodo `.next`.

### ResultSet.TYPE_SCROLL_INSENSITIVE

---

È possibile utilizzare anche i metodi `.previous`, `.first`, `.last`, [ecc](ResultSets%20&%20Statements%209e909136982749de8764d3872e4250d0.md).

Se vengono apportate modifiche alla tabella a cui si riferisce il `ResultSet`, quest’ultimo non rifletterà tali modifiche.

### ResultSet.TYPE_SCROLL_SENSITIVE

---

È possibile utilizzare anche i metodi `.previous`, `.first`, `.last`, 

In questo caso il `ResultSet` verrà automaticamente aggiornato.

### `ResultSet` aggiornabili

---

Esistono dei metodi `.updateXXX`, simili ai metodi `getXXX`, che andranno a aggiornare i valori all’interno della riga a cui punta il cursore del `ResultSet`.

`void updateXXX(int columnIndex, XXX newValue); void updateXXX(String columnName, XXX newValue);`

Il primo parametro può essere:

una stringa che contiene il nome della colonna

l’indice della colonna

Il secondo parametro sarà il nuovo valore assunto dal record a cui punta il cursore del `ResultSet`, alla colonna indicata.

---

Il metodo `.deleteRow` dell’interfaccia `ResultSet` elimina la riga a cui punta il cursore, questo metodo ha effetto **sia sul `ResultSet`** **che sulla tabella associata nel database**.