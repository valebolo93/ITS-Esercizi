'''Un'applicazione interessante dei computer è la rappresentazione grafica di dati.
Scrivere un programma che acquisisca cinque numeri interi (ognuno compreso tra 1 e 30) e 
visualizzi in output un grafico a barre testuale con asterischi *.

Per ogni numero letto, il programma deve stampare una riga contenente tanti asterischi quanti il valore del numero stesso.'''

#ho creato la variabile numeri interi, una lista vuota, il contatore e la variabile numeri interi che deve essere compreso tra 1 e 30
numeri_interi:int=int(input())
numeri_interi= 1>numeri_interi<30
i=1
lista:list[int]=[]
#Qui ho utilizzato un ciclo while in cui i numeri inseriti massimo possono essere 5 e vengono aggiunti alla lista con la funzione append
while True:
    numeri_interi:int=int(input())
    lista.append(numeri_interi)
    i=i+1
    if i>=5:
        break


 # qui ho provato senza successo, a far coincidere gli asterischi al valore inserito. Ma vengono 5 asterischi per tutti e 5 i numeri
for i in range(len(lista)):
    asterisco = "*"
    
    equivalenza= asterisco*(len(lista))
    print(equivalenza)

