---
author: Simone Parente Martone
---

È un API standard per operare con basi di dati relazionali in JAVA, base per altri package di più alto livello

Lo scopo principale è quello di permettere una comunicazione tra un applicativo JAVA e un database

### Schema

- Java Application
- JDBC API
- JDBC Driver Manager (Oracle, SQL Server, MySQL)

# Storia delle architetture Client-Server

## Accesso diretto

---

![accesso diretto.png](accesso_diretto.png)

### Vantaggi

---

- Efficiente per soluzioni molti piccole

### Svantaggi

---

- Sviluppo molto lento
- Non flessibile/scalabile
- Non condivisibile
- Distoglie l’attenzione dalla business logic

## Architetture 2-tier

---

![2tier.png](2tier.png)

### Svantaggi

---

- Sicurezza
- # licenze per DBMS
- GUI legata a business logic
- Non utilizzabile sul web

### Vantaggi

---

- Molto più efficiente
- Sviluppo rapido
- Scalabile/flessibile

## Architetture 3-tier

---

![3tier.png](3tier.png)

### Vantaggi

---

- Policy sicurezza
- GUI indipendente dai dati
- Web-Oriented

### Svantaggi

---

- Maggiore complessità

## Come gestire la connessione col DBMS

---

### Embedded SQL

---

- Il programma colloquia direttamente col DBMS (middle-ware e librerie accesso dati dell’architettura 3 tier non sono presenti)
- Gli statement SQL sono compilati usando un precompilatore specifico del DBMS
- SQL Diviene parte integrante del codice

### Call Level Interface (quella che ci interessa)

---

- Il programma accede al DBMS tramite un’interfaccia standard
- Gli statement SQL non sono compilati ma inviati al DBMS a runtime
- Il DBMS può essere sostituito e la stessa interfaccia può interagire con più DBMS
- Esempi di Call Level Interface
    - ODBC
        - Open Database Connectivity
    - OLE-DB
        - Object Linking ad Embedding for Databases
    - ADO
        - ActiveX Data Objects
    - UDA
        - Universal Data Access
    - JDBC
        - Java DataBase Connectivity

---

## ODBC (Open DataBase Connectivity)

---

![odbc.png](odbc.png)

API Standard definita da Microsoft nel 1992, permette l’accesso a dati residenti in diversi DMBS e gestisce le richieste SQL convertendole nel linguaggio adatto al DBMS utilizzato, così che gli sviluppatori possano formulare richieste SQL senza dover conoscere le interfacce di programmazione proprietarie di ogni singolo database

### Svantaggi:

- Utilizza interfacce C
- È procedurale (non object oriented)
- Ha poche funzioni con pochi parametri

# Java DataBase Connectivity

---

Il motivo per cui utilizziamo JDBC sono diversi:

- I database sono il core-system della maggior parte dei sistemi client-server

- Quasi la totalità delle entità necessita di accedere a un database e vogliamo che tale accesso sia:

- Closs-platform (scritto in JAVA)
- Capace di interagire con qualsiasi R-DBMS

## Cosa fa JDBC

---

JDBC permette ad oggetti Java di dialogare con database relazionali ed effettua tre operazioni fondamentali

1. Stabilisce una connessione con il database

1. Invia statements SQL

1. Processa i risultati

## Punti chiave

---

- Non necessita di driver preinstallati (ODBC invece si)
- Utilizza la sintassi degli URL per la localizzazione delle risorse
- Una classe speciale (**DriverManager**) è responsabile di attivare il driver giusto per la connessione ad un R-DBMS
- Mappa tutti i tipi SQL in tipi Java

# JDBC Drivers

## Driver tipo 1

---

![driver tipo 1.png](driver_tipo_1.png)

Wrapper (fa da tramite) da JDBC ad ODBC

Traduce le calls JDBC in ODBC calls

### Vantaggi

---

- È incluso nel JDK
- Funziona con qualsiasi DBMS ODBC
- Facile da configurare

### Svantaggi

---

- Richiede l’installazione del bridge JDBC-ODBC
- Molto lento
- Utilizzabile solo per sviluppo di codice

## Driver tipo 2

---

![driver tipo 2.png](driver_tipo_2.png)

Wrapper da JDBC a driver nativo DBMS

Traduce le JDBC calls in chiamate JNI al codice C/C++ del DBMS driver

### Vantaggi

---

- Facile da realizzare
- Fa uso di driver preesistenti

### Svantaggi

---

- Un bug nel driver può portare in crash il sistema
- Difficile da configurare
- Non adatto a Web-App

## Driver tipo 3

---

![driver tipo 3.png](driver_tipo_3.png)

Driver Pure Java per Database Middleware

Traduce le JDBC calls in un net che viene convertito poi nel DBMS-protocol indipendente dal DBMS e dal server

### Vantaggi

---

- Pure Java
- Un unico driver client per N DMBS lato server

### Svantaggi

---

- Difficile da configurare
- I DMBS vendors non realizzano questo tipo di driver
- Costoso

## Driver tipo 4

---

![driver tipo 4.png](driver_tipo_4.png)

Driver Pure Java per DBMS

Traduce le JDBC calls in un net-protocol comprensibile dal DMBS

### Vantaggi

---

- Massima velocità
- Facile da configurare
- Pure Java

### Svantaggi

---

- Non supportato da tutti i DBMS
- Richiede un driver per ogni DBMS, lato client

# JDBC API

---

## Struttura di JDBC

---

![struttura jdbc.png](struttura_jdbc.png)

JDBC è costituito da 2 layer principali

1. JDBC driver (verso il DBMS)
2. JDBC API (verso l’applicativo)
- Class Diagram di JDBC
    
![jdbc uml.png](jdbc_uml.png)


Tutte le classi fondamentali di JDBC sono interfacce, non implementate in JDBC ma implementate dallo specifico driver

![Interface-Implementation pattern](interfacce_imp_pattern.png)

Interface-Implementation pattern

# [Connessione.Java](http://Connessione.Java) (PostgreS)

```java
import java.sql.*;
import java.util.Scanner;

public class Connessione
{
    private ConnessioneDB() throws SQLException {
        try {
            String driver = "org.postgresql.Driver";
            Class.forName(driver);
            String nome = "postgres";
            String password = "1234";
            // postgres è il nome del database
            String url = "jdbc:postgresql://localhost:5432/postgres"; //5432 è la porta del database
            connection = DriverManager.getConnection(url, nome, password);

        } catch (ClassNotFoundException ex) {
            System.out.println("Database Connection Creation Failed : " + ex.getMessage());
            ex.printStackTrace();
        }

    }
}
```

## Preparazione

---

1. Importare le classi

```java
import java.sql.*
```

1. Usare i blocchi `try`, `catch`.

Il primo blocco `try` contiene il metodo `Class.forName` (package `java.Lang`), il metodo lancia un `ClassNotFoundException` che il blocco `catch` potrà gestire subito dopo(può essere gestita solo una volta nel costruttore)

Il secondo blocco `try` contiene i metodi JDBC, che lanciano tutti un eccezione del tipo `SQLException` così che il blocco `catch` possa gestire solo oggetti di quel tipo

## 1. Caricare il driver

---

```java
import java.sql.*;

try
{
Class.forName("org.postgresql.Driver"/*NOME_DRIVER*/);
}

catch(ClassNotFoundException)
{
//driver non trovato
}
```

Il DriverManager mantiene una lista di classi `Driver` che registrano se stessi invocando il metodo `registerDriver()`. L’inizializzatore statico del driver, chiamato dalla JVM al caricamento della classe, si registra nel DriverManager

```java
public class MyDriver
{
	static
		{
			new MyDriver();
		}
	public MyDriver()
		{
			java.sql.DriverManager.register(this);
		}
}
```

## 2. Ottenere una connessione

---

```java
Connection conn= DriverManager.getConnection(URL_Database);
```

L’oggetto Connection rappresenta un canale di comunicazione con un DB

È richiesta una connessione al Driver Manager, senza specificare quale particolare Driver debba istanziarla in modo tale da ottenere una completa indipendenza dal DBMS!

### Gli URL in JDBC

---

Un URL in JDBC è una stringa formata da nodi, separati da ‘:’ oppure ‘/’

- Formato
    
    protocollo:sottoprotocollo:databasename
    
    In particolare il parametro databasename non ha una sintassi specifica, bensì viene interpretato dal driver
    
    - Esempi
        - jdbc:odbc:myDB
        - jdbc:oracle:@mywebsite:1521:myDB
        - jdbc:cloudscape:myDB
        - jdbc:cloudscape:rmi:myDB;create=true
- 

# Interfacce

---

## Driver

---

## DriverManager

---

![driver.png](driver.png)

![drivermanager.png](drivermanager.png)

## Classe DriverManager

## Interfaccia Statement

---

![classe drivermanager.png](classe_drivermanager.png)

![statement.png](statement.png)

## 3. Eseguire uno statement

---

Uno statement è un object che invia le istruzioni SQL alla Connection, verso il DB, unico per tutta la durata della connessione, per fare una nuova query bisogna cambiare la stringa all’interno dell’object (può essere una variabile String ovviamente)

```java
try{
Statement st=con.createStatement();
ResultSet rs=st.executeQUERY("SELECT nome FROM studenti");
}
catch(SQLException sqe)
{
//problema
}
```

La classe statement ha come compito principale quello di eseguire query SQL

- Metodi
    - executeQuery() per gli statement che devono restituire tuple
    - executeUpdate() per gli statement che non restituiscono tuple (INSERT, DELETE, UPDATE)
    - executeBatch() per eseguire più statement in sequenza
    - Se non sappiamo che tipo di query utilizzeremo, si usa la funzione execute()
        - restituisce true se è disponibile un ResultSet
        - Si deve chiamare la getResult() per recuperare le informazioni
        - A ogni statement è associato un unico ResultSet
    - getMoreResults (bool): Moves to this Statement object's next result, returns true if it is a ResultSet object, and implicitly closes any current ResultSet object(s) obtained with the method getResultSet

### Prepared Statements

---

Sono statement precompilati (che il dbms salva nella propria cache), vengono usati per query simili nella struttura, in cui cambiano principalmente i parametri così da ottenere un miglioramento di prestazioni se la query è eseguita molto spesso

```java
PreparedStatement updateEsami=con.prepareStatement(
"UPDATE Studenti SET esami = ? WHERE Matricola LIKE ? ");
updateEsami.setInt(1, 13); 
updateEsami.setString(2, ”011/245389"); 
updateEsami.executeUpdate();
```

### Callable Statements (per funzioni)

---

Classe JDBC per supportare le stored procedures (che vengono utilizzate per incapsulare insiemi di operazioni da eseguire su database server) e l’utilizzo è richiesto solo per stored procedures che restituiscono valori 

## 4. Gestire i risultati

---

I risultati di una query sono salvati in un object ResultSet

### ResultSet

---

Ha un cursore che punta al record corrente, inizialmente è posizionato esternamente “rispetto alla lista”, così che possa controllare se esista un prossimo risultato utile.

- Navigazione del Resultset
    
    Si utilizzano i metodi
    
    - `first()`
    - `previous()`
    - `absolute(int)`
    
    - `last()`
    - `beforeFirst()`
    - `relative(int)`
    
    - `next()`
    - `afterLast()`
    

Per modificare un Resultset si usa il metodo `rs.update(parametri)` o `rs.updaterow()`

Per determinare se un valore restituito è tipo `null` bisogna leggere la colonna e usare il metodo `ResultSet.wasNull()` che ritorna un tipo boolean.

## 5. Rilasciare le risorse

---

```java
rs.close() //chiude l'object ResultSet

st.close() //Chiude l'object Statement

con.close() //Chiude la connessione
```

### DatabaseMetaData

---

Interfaccia utilizzata per reperire informazioni sulle sorgenti dei dati, mette a disposizione circa 150 metodi classificati nelle seguenti categorie:

- informazioni generali sulla sorgente dei dati
- aspetti e capacità supportate dalla sorgente dati
- limite della sorgente dati
- cosa gli object SQL contengono e gli attributi di questi object
- 

### ResultSetMetadata

---

Tra le informazioni troviamo:

- Numero di colonne (`getColumnCount()`)
- Numero di una colonna(`getColumnLabel()`)
- Tipo di una colonna (`getColumnTypeName()`)

```java
ResultSetMetaData md=rs.getMetaData();
```

## Transazioni

---

Insiemi di statement raggruppati in un’unità logica inscindibile

Ogni statement deve andare a buon fine altrimenti l’intera transazione verrà annullata(rollback)

### API JDBC per transazioni

---

Di default ogni operazione è una transazione, per eseguire diversi statement in una singola transazione si usa 

```java
con.setAutoCommit(false)
//statements
con.commit()
```

# Exceptions e Warning

---

Quasi tutte le istruzioni viste finora possono portare a potenziali problemi, in alcuni casi non c’è nulla che possiamo fare per evitarli o gestirli

## SQLException

---

![sqlexception.png](sqlexception.png)

È una sottoclasse di `Java.lang.Exception` che aggiunge informazioni sul tipo di errore proveniente dal database, è bene notare che diverse eccezioni potrebbero concatenarsi.

## SQLWarning

---

![sqlwarning.png](sqlwarning.png)

È una sottoclasse di SQLException che non richiede il catch e viene utilizzato nel momento in cui il problema non sia grave al punto da dover fermare l’esecuzione del metodo

(Esaminabile con il metodo getWarnings() di Connection,
Statement, ResultSet)