'''Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall’utente.

Il programma deve:

acquisire una sequenza di numeri interi, terminando l’inserimento quando l’utente digita 0 (che non deve essere considerato nei calcoli);
calcolare e visualizzare la somma di tutti i numeri pari inseriti;
calcolare e visualizzare la media di tutti i numeri dispari inseriti;
determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
se più numeri hanno la stessa frequenza massima, visualizzarli tutti.'''

lista:any=[]
numeri=any(input())
somma=0
media=0
i=1
numeri_pari= numeri%2==0
numeri_dispari= numeri%2!=0

while True:
    numeri=any(input())
    if numeri %2==0:
            numeri.append(lista)
            somma= sum(numeri_pari + i)
            i=i+1
            print(somma)

    if numeri%2!=0:
         media= numeri_dispari/i
         i=i+1
         print(media)

    if numeri ==0:
        break
