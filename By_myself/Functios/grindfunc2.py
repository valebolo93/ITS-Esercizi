'''Scrivi una funzione che prende una stringa e restituisce la stringa invertita.'''

stringa:str=input("Inserisci una stringa: ")

def inserire_stringa(stringa) -> str:
    for stringhe in stringa:
        invertita=(stringa[::-1])
    return invertita

print(inserire_stringa(stringa))