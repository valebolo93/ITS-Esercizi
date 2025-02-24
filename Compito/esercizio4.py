'''Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi 
(sia interi che decimali). L'inserimento termina quando viene fornito un numero negativo, 
che funge da sentinella e non deve essere considerato nei calcoli.
Il programma deve:

    Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
    Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti (sia interi che decimali).
'''

'''Expected Output:
n=5
read x
x:float=>0
if x<0
break'''

numeri:str= float(input("inserire numeri: "))
media_numeri=0

n=[]
n_interi=[]


#ho inserito un ciclo per cui se i numeri sono positivi, vengono inseriti nella lista n

while numeri>=0:
    numeri:any= (input("inserire numeri: "))
    print(type(numeri))
    n.append(any(numeri))



'''qui ho provato ad utilizzare la funzione integer per verificare se il numero fosse intero e aggiungerlo alla lista degli interi
non riesco a risolvere questo errore: TypeError: '>=' not supported between instances of 'str' and 'int'''


if numeri.is_integer():
    n_interi.append(int(numeri))
    media_numeri=sum(n_interi)/len(n_interi)
    print(f"la tua media numeri sarà: {numeri}")

#se i numeri inseriti sono negativi, il programma si blocca
while numeri<0:
    print("Hai inserito un valore negativo")
    break


#ho provato a calcolare il min e il max tra i valori all'interno della lista n
if n:
    min_num=min(n)
    max_num=max(n)
    print(type(numeri))

       




