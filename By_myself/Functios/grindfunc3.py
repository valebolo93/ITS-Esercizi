'''Scrivi una funzione che prende una lista di parole e restituisce una lista 
contenente solo le parole che iniziano con una lettera specificata.'''

from typing import Any
from typing import List

lista:list=[]

def function_list(lista:list,lettera:str="a") -> list:
    for stringhe in lista:
        if lista[0] == lettera:
         lista.append(stringhe)
        return lettera in lista
        

function_list("Valentina","solo")
print(function_list(list))