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

n:int= 5
i=1
x=0
sum=0
media=0

while True:
    if x>0:
        x:int=int(input())
        sum=0
        media=0
        media=sum+i
        i=i+1
        if x<0:
            break