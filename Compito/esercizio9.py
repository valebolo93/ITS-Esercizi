'''Il valore di π può essere approssimato utilizzando la seguente serie infinita:

π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

Scrivere un programma che calcoli il valore di π utilizzando questa serie e determini quanti termini sono necessari 
per ottenere approssimazioni sempre più accurate. Quindi:

progettare un algoritmo che mostri in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.141;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.1415;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14159.
Nota: Il programma deve iterare fino a raggiungere ciascuna delle soglie indicate, contando il numero di termini necessari.'''

#Ho inziatilizzato le varie variabili, inserito una lista vuota dove inserire i risultati e inserito un contatore
denominatore:any= 1
numeratore:any= 4
frazione:any= 4/1
i=1
risultati= [3.14, 3.141,3.1415,3.14159]
lista:list[any]=[]
results= 1

#ho inserito il ciclo while per provare a salvare ogni nuovo risultato dentro la lista aggiornando il contatore

while True:
    denominatore+= 2
    nuovo:any= frazione / denominatore
    lista.append(nuovo)
    i=i+1
    
#auspicavo si bloccasse il ciclo una volta ottenuto i risultati richiesti
    if nuovo== risultati[0]:
        break
    if nuovo== risultati[1]:
        break
    elif nuovo==risultati[2]:
        break
    elif nuovo==risultati[3]:
        break

    




