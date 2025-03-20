''' Start with a copy of your program from Exercise 8-9. Write a function called send_messages() 
that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages were moved correctly.'''

#lista esistente
lista:list=["Come va?",
            "Ti voglio bene",
            "Forza Roma",
            "W l'estate"]
#lista nuova vuota
sent_messages:list=[]


#funzione che mi stampa ogni singolo messaggio
def send_messages(lista) -> None:
    
    return lista
print(send_messages(lista[0]))
print(send_messages(lista[1]))
print(send_messages(lista[2]))
print(send_messages(lista[3]))

print("----------------------------------------")
#ciclo for per aggiungere gli elementi della lista nella lista sent messages
for items in lista:
    sent_messages.append(items)
    

for items in lista:
    lista.pop(0)
    lista.pop(0)

print(sent_messages)
print("----------------------------------------")
print(lista)





 
    


