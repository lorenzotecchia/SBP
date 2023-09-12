---
Date: November 10, 2022
Number: 18
Reviewed: Yes
Status: Done
author: Simone Parente Martone
---
# Trigger

---

Un trigger è una funzione di manutenzione della base di dati, a differenza delle funzioni standard non viene invocata, bensì è scatenata da una serie di eventi che avvengono all’interno della base di dati. Gli eventi che in particolare ci interessano sono:

- `INSERT`

- `UPDATE`

- `DELETE`

Un trigger è composto da tre elementi

1. ************Evento************ che scatena il trigger, esso è generalmente una operazione di aggiornamento della base di dati (`INSERT`, `UPDATE`, `DELETE`).
2. **********************Condizione********************** che determina se una azione deve essere eseguita, può anche non essere presente così che l’azione venga eseguita ogni volta che si verifichi l’evento.
3. ************Azione************ da intraprendere al verificarsi dell’evento, può essere una procedura SQL ma anche l’esecuzione di un programma esterno.

## Bisogna definire una serie di parametri:

---

- Quale evento scatena la reazione?
- Condizioni di filtraggio che mi permettono di definire con precisione quale evento scatena l’azione
- Se l’operazione è globale
- Reazione

- Quando deve essere scatenata la reazione? Prima o dopo l’evento?
    - Prima: Ci sarà una delete e voglio eseguire dei comandi prima che la tupla venga eliminata
    - Dopo: C’è stato un UPDATE e voglio propagare l’evento

## Sintassi

---

```sql
CREATE TRIGGER <nomeTrigger>
[AFTER/BEFORE/INSTEAD OF] <operazione>
[FOR EACH ROW]
[WHEN <condizione>]
BEGIN
<CORPO DELLA PROCEDURA>
END
```

Le [] indicano [**Istruzioni facoltative**]

- `AFTER` indica che deve essere attivata dopo il verificarsi degli eventi
- `BEFORE` indica che la regola deve essere attivata prima del verificarsi degli eventi
- `INSTEAD OF` esegue il trigger invece dell’evento

`[FOR EACH ROW]` Indica che la regola influenzerà tutte le tuple influenzate dall’evento, in assenza di questa clausola l’azione verrà eseguita una sola volta, anche se diverse righe sono state influenzate dall’evento. L’uso della clausola attiva **due speciali variabili**:

### $\cdot$ NEW

Permette di riferirsi alla tupla appena inserita/aggiornata (in caso di `INSERT` o `UPDATE`)

### $\cdot$  OLD

Permette di riferirsi alla tupla che è stata eliminata oppure a quest’ultima prima dell’aggiornamento (`DELETE` o `UPDATE`)

`WHEN <condizione>` specifica la condizione che deve essere controllata dopo che la regola è innescata, MA prima che l’azione sia eseguita

- Esempi di utilizzo
    
    
    Base di dati dei seguenti esempi
    
    Stip_totale è un attributo derivato che deve essere aggiornato così da mantenere consistente il valore all’interno di un dato dipartimento
    
    Eventi che possono causare un cambiamento:
    
    - 1. Inserimento di un nuovo impiegato in un dato dipartimento
        
        ```sql
        CREATE TRIGGER StipTotale1
        AFTER INSERT ON Impiegato
        FOR EACH ROW
        WHEN(NEW.Num_D IS NOT NULL)
        		UPDATE Dipartimento
        		SET Stip_Totale=Stip_Totale+NEW.Stipendio
        		WHERE Num_D=NEW_Num_D
        ```
        
    - 2. Cambiamento dello stipendio di uno o più impiegati
        
        ```sql
        CREATE TRIGGER StipTotale2
        AFTER UPDATE OF Stipendio ON Impiegato
        FOR EACH ROW
        WHEN(New.Num_D IS NOT NULL)
        		UPDATE Dipartimento
        		SET Stip_Totale=Stip_Totale + NEW.Stipendio - OLD.Stipendio
        		WHERE Num_D=NEW.Num_D
        ```
        
    - 3. Il passaggio di un impiegato da un dipartimento ad un altro
        
        ```sql
        CREATE TRIGGER StipTotale3
        AFTER UPDATE OF Stipendio ON Impiegato
        FOR EACH ROW
        BEGIN
        	UPDATE Dipartimento
        	SET Stip_Totale = Stip_Totale + **NEW**.Stipendio
        	WHERE Num_D=**NEW**.Num_D
        	UPDATE Dipartimento
        	SET Stip_Totale= Stip_Totale - **OLD**.Stipendio
        	WHERE Num_D=******OLD******.Num_D
        END;
        ```
        
    - 4. Lo stipendio totale deve essere ricalcolato nel caso in cui un impiegato venisse licenziato o lasciasse il dipartimento
        
        ```sql
        CREATE TRIGGER StipTotale4
        AFTER DELETE ON Impiegato
        FOR EACH ROW
        WHEN(OLD.Num_D IS NOT NULL)
        	UPDATE Dipartimento
        	SET Stip_Totale = Stip_Totale - **OLD**.Stipendio
        	WHERE Num_D=**OLD**.Num_D
        ```
        
    - 5. Vogliamo rilevare tutte le volte che lo stipendio di un impiegato supera quello del suo supervisore
        
        Eventi che possono innescare questo evento
        
        - Inserimento di un nuovo impiegato
        - Modifica di stipendio
        - Modifica di dipartimento di un impiegato
        
        Supponiamo che l’azione da eseguire è una procedura chiamata “SUPER_INFORM” che informa il superiore dell’evento
        
        ```sql
        CREATE TRIGGER Super_Inform
        BEFORE INSERT OR UPDATE OF Stipendio, SSN_Super ON Impiegato
        FOR EACH ROW
        WHEN(NEW.Stipendio>(SELECT Stipendio
        											FROM Impiegato
        											WHERE SSN=**NEW**.SSN_SUPER))
        SUPER_INFORM(NEW.SSN_SUPER, NEW.SSN)
        ```