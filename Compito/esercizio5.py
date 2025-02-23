'''Si supponga di poter acquistare barrette di cioccolato da un distributore automatico al costo di 1 euro ciascuna. Ogni barretta acquistata contiene un buono sconto, e con 6 buoni sconto si ottiene una barretta gratuita.

Scrivere un programma che:

Acquisisca in input un valore N (numero di euro disponibili).
Calcoli e mostri in output il numero totale di barrette che si possono ottenere, considerando anche quelle ottenute con i buoni sconto.
Mostri quanti buoni sconto avanzano al termine dell'acquisto.'''



barrette:int= 0
buoni_sconto:int=0

while True:
    euro:int= int(input("Quanti soldi hai disponibili: "))
    barrette=euro
    
    if euro==0:
        print("Soldi terminati")
        break
    if euro>=6:
        buoni_sconto=euro
        barretta_bonus=buoni_sconto//6
        barrette+=barretta_bonus
        buoni_sconto=buoni_sconto%6

    if euro <6:
        buoni_sconto=euro
        barretta_bonus=buoni_sconto//6
        barrette+=barretta_bonus
        buoni_sconto=buoni_sconto%6

    


        print(f"Il numero totale delle barrette che si possono ottenere è: {barrette}")
        print(f"I buoni sconti che rimangono sono: {buoni_sconto}")