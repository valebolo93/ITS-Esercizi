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

'''numeri_reali:any=0
numeri_interi:int=0
x=0

while x>0:
        numeri_reali=(input())
        sum=0
        media=0
        i=1
        sum=sum+numeri_reali
        media=sum//i
        i=i+1
        else:
        if x<0:
              print(f"programma terminato")'''


numeri= float(input("inserire numeri: "))
while True:
    i=1
    sum=0
    media=0
    numeri>=0
    if numeri.is_integer():
        print("Numero intero")
        media+=numeri
        i=i+1
    else:
        print("Numero decimale")
       






        