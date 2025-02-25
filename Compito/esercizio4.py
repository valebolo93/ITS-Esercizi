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

#qui ho inizializzato le mie variabili e creato delle liste dove poi andrò ad inserire i numeri
numeri:str= float(input("inserire numeri: "))
media_numeri:float=0
max_num=0
min_num=0
i=1
n=[]
n_interi=[]
somma_interi=0


#ho inserito una condizione per cui se i numeri sono positivi, vengono inseriti nella lista n
while True:
    if numeri>=0:
        numeri:str= float(input("inserire numeri: "))
        print(type(numeri))
        n.append(numeri)
        i=i+1

        
        if numeri.is_integer():
            n_interi.append(int(numeri))
            somma_interi += numeri
            media_numeri +=1
            media_numeri = somma_interi/n_interi
            i=i+1
            print(f"la tua media numeri sarà: {media_numeri}")

#se i numeri inseriti sono negativi, si aggiorna la lista n e il programma si blocca. Il break non lo posso utilizzare in questo caso
            if numeri<0:
                n.append(int(numeri))
                print("Hai inserito un valore negativo")
                break
    


#ho provato a calcolare il min e il max tra i valori all'interno delle lista n e n_interi 
                if n:
                    min_num=min(n,n_interi)
                    max_num=max(n,n_interi)
                    print(f"Il numero più grande è {max_num}")
                    print(f"Il numero più grande è {min_num}")

       




