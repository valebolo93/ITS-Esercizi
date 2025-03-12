'''Scrivi una funzione che prende una lista di parole e restituisce una lista contenente la lunghezza di ciascuna parola.'''

lista:list= ["casa","banana","ciao","vale","ortopedico"]

def lung_parole(lista:list) ->list:
    return len(lista)
    
for parole in lista:
    print(f"La lunghezza delle parole è: {len(parole)}")
