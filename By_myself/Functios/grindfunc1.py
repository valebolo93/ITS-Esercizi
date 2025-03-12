'''Scrivi una funzione che prende una lista di numeri e restituisce la somma di tutti gli elementi.'''

lista:list=[1,2,3,4,5,6,7,8,9,10]

def somma_num(lista:list) -> int:
    somma=0
    for numeri in lista:
        somma=somma + numeri
    return somma
    
print(somma_num(lista))