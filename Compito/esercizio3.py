'''Scrivere un programma che acquisisca una stringa inserita dall'utente e generi una nuova stringa 
che corrisponda alla versione invertita della stringa originale. Il programma deve poi visualizzare la stringa ottenuta in output. 
Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente i cicli.'''

#Ho inserito una prima stringa con l'input che verrà dato dall'ultente
stringa:str= (input("Inserisci una stringa: "))

#Ho poi utilizzato un ciclo for e inizializzato una nuova variabile stringa per andare a invertire quella originale
for parola in stringa:
    stringa1= stringa[::-1]
    print(stringa1)
    break




