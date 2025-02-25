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
n=0
n_interi=numeri
n_decimali=numeri
somma_interi=0
i=1

#ho inserito un ciclo per i numeri positivi. 
while True:
    if numeri>=0:
        numeri:str= float(input("inserire numeri: "))
        print(type(numeri))
        i=i+1
#Se i numeri sono interi, l'iterazione permette di fare la media dei numeri, in caso contrario agisce l'else
        
        if numeri.is_integer():
            n_interi=n_interi+numeri
            somma_interi = somma_interi+n_interi
            media_numeri = somma_interi/i
            i=i+1
            print(f"la tua media numeri sarà: {media_numeri}")

        else:
            n_decimali= n_decimali+numeri


#se i numeri inseriti sono negativi, il programma si blocca con il break
            if numeri<0:
                print("Hai inserito un valore negativo")
                break
    
#Ho calcolato il min e il max tra i valori interi e decimali
        if numeri:
            min_num=min(n_interi,n_decimali)
            max_num=max(n_interi,n_decimali)
            print(f"Il numero più grande è {max_num}")
            print(f"Il numero più piccolo è {min_num}")

       




