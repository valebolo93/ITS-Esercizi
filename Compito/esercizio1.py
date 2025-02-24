'''Scrivere un programma che permetta all'utente di inserire una serie di parole in input, 
terminando l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione).
Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e visualizzare un messaggio corrispondente.'''

#Ho ultilizzato il ciclo while per inserire parole fino a quando non viene inserita la parola fine che fa terminare il ciclo.
while True:
    parola=input("Inserisci una serie di parole:  ")
    if parola== "fine":
        break

#Ho utilizzato la condizione if per verificare se la prima e ultima lettera della parola sono uguali, altrimenti viene utilizzato l'else.
    if parola[0]==parola[-1]:
        print(f"Il primo e ultimo carattere sono uguali")
    else:
        print(f"Il primo e ultimo carattere non sono uguali")