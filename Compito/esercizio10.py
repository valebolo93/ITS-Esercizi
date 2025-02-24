'''Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall’utente.

Il programma deve:

acquisire una sequenza di numeri interi, terminando l’inserimento quando l’utente digita 0 (che non deve essere considerato nei calcoli);
calcolare e visualizzare la somma di tutti i numeri pari inseriti;
calcolare e visualizzare la media di tutti i numeri dispari inseriti;
determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
se più numeri hanno la stessa frequenza massima, visualizzarli tutti.'''
#ho iniziatizzato tutte le mie variabili, comprese numeri pari e dispari 
lista:any=[]
somma=0
media=0
i=1
numeri=0
#nel mio ragionamento volevo far coincidere le due variabili rispettivamente con i numeri pari e dispari
numeri_pari=0
numeri_dispari=0
numeri_pari==numeri%2==0
numeri_dispari==numeri%2!=0

#qui ho tentato di utilizzare un ciclo while e fare come nei diagrammi ma purtroppo non mi escono i giusti risultati
while True:
    numeri=any(input())
    if numeri_pari:
            somma= sum(any(numeri_pari + i))
            i=i+1
            print(somma)

    if numeri_dispari:
         numeri=any(input())
         media= sum(any(numeri_dispari/i))
         i=i+1
         print(media)

    if numeri==0:
        print(f"{numeri} termina")
        break
