'''Scrivi una funzione che prende una lista di parole e restituisce una lista 
contenente solo le parole che iniziano con una lettera specificata.'''

from typing import Any

lista_vecchia:list=["Sole","cane", "ancora", "aria", "aspro"]

def function_list(lista_vecchia:list, lettera:str="a") -> list:
    lista_nuova:list = []
    for parola in lista_vecchia:
        if parola[0] == lettera:
            lista_nuova.append(parola)
    return lista_nuova
        

lista_nuova = function_list(lista_vecchia, "a")
print(lista_nuova)