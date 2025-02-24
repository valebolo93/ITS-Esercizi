'''Si supponga di poter acquistare barrette di cioccolato da un distributore automatico al costo di 1 euro ciascuna. Ogni barretta acquistata
 contiene un buono sconto, e con 6 buoni sconto si ottiene una barretta gratuita.

Scrivere un programma che:

Acquisisca in input un valore N (numero di euro disponibili).
Calcoli e mostri in output il numero totale di barrette che si possono ottenere, considerando anche quelle ottenute con i buoni sconto.
Mostri quanti buoni sconto avanzano al termine dell'acquisto.'''

#Ho inizializzato le variabili barrette e buoni_sconto

barrette:int= 0
buoni_sconto:int=0

#Ho utilizzato il ciclo while per far inserire gli euro disponibili dall'ultente e la variabile barrette coincidente con gli euro inseriti
while True:
    euro:int= int(input("Quanti soldi hai disponibili: "))
    barrette=euro
    
    #Ho inserito la condizione per cui se gli euro sono uguali a 0, il programma riconosce che i soldi sono terminati
    if euro==0:
        print("Soldi terminati")
        break

    #Se gli euro sono maggiori o uguali a 6, ogni barretta equivale a un buono sconto che col floor division calcola la parte intera più vicina al 
    #risultato. Per ogni barretta, viene aggiunta una barretta bonus. L'ultima riga di codice= buoni_sconto=buoni_sconto%6 mi è stata suggerita 
    if euro>=6:
        buoni_sconto= barrette
        barretta_bonus=buoni_sconto//6
        barrette+=barretta_bonus
        buoni_sconto=buoni_sconto%6
        print(f"Il numero totale delle barrette che si possono ottenere è: {barrette}")
        print(f"I buoni sconti che rimangono sono: {buoni_sconto}")

    if euro <6:
        buoni_sconto=barrette
        barretta_bonus=0
        barrette+=barretta_bonus
        buoni_sconto=buoni_sconto%6
    print(f"Il numero totale delle barrette che si possono ottenere è: {barrette}")
    print(f"I buoni sconti che rimangono sono: {buoni_sconto}")