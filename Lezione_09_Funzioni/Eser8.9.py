'''Make a list containing a series of short text messages. 
Pass the list to a function called show_messages(), which prints each text message.'''
lista:list=["Come va?",
            "Ti voglio bene",
            "Forza Roma",
            "W l'estate"]

def show_messages(lista):
    return lista


for items in lista:
    print(show_messages(lista[0]))
    print(show_messages(lista[1]))
    print(show_messages(lista[2]))
    print(show_messages(lista[3]))
    break
