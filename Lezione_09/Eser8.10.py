''' Start with a copy of your program from Exercise 8-9. Write a function called send_messages() 
that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages were moved correctly.'''

#lista esistente
lista:list=["Come va?",
            "Ti voglio bene",
            "Forza Roma",
            "W l'estate"]

sent_messages:list=[]



#funzione
def send_messages(lista):
    return lista
print(send_messages(lista[0]))
print(send_messages(lista[1]))
print(send_messages(lista[2]))
print(send_messages(lista[3]))

print("----------------------------------------")
for items in lista:
    sent_messages.append(items)
    

for items in lista:
    lista.pop(0)
    lista.pop(0)

print(sent_messages)
print("----------------------------------------")
print(lista)





 
    


