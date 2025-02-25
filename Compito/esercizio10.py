'''Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall’utente.

Il programma deve:

acquisire una sequenza di numeri interi, terminando l’inserimento quando l’utente digita 0 (che non deve essere considerato nei calcoli);
calcolare e visualizzare la somma di tutti i numeri pari inseriti;
calcolare e visualizzare la media di tutti i numeri dispari inseriti;
determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
se più numeri hanno la stessa frequenza massima, visualizzarli tutti.'''
#ho iniziatizzato tutte le mie variabili, comprese numeri pari e dispari 

somma:float=0
media:float=0
i=1
numero_max = 0
numero_min = 0

#nel mio ragionamento volevo far coincidere le due variabili rispettivamente con i numeri pari e dispari
'''numeri_pari=0
numeri_dispari=0
numeri_pari=numeri%2==0
numeri_dispari=numeri%2!=0'''

#qui ho tentato di utilizzare un ciclo while e fare come nei diagrammi ma purtroppo non mi escono i giusti risultati
while True:

    numeri:float = float(input("Inserisci un numero: "))

    if numeri == 0:
        break
    
    if numeri.is_integer():
        somma= somma+numeri
        i=i+1

    else:
        if numeri > numero_max:
            numero_max = numeri
        if numeri < numero_min:
            numero_min = numeri

if numeri > 0:
    media = somma / i
    print(f"La media dei numeri è: {media:.2f}")

if numero_max != float('-inf') and numero_min != float('inf'):
    print(numero_max)
    print(numero_min)
              
                      