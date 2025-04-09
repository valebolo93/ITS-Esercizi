'''Scrivere in Python una funzione recursivePower che calcola la potenza di un numero 
utilizzando la ricorsione. La funzione deve ricevere due parametri in input:

    base: il numero da elevare a potenza.
    exponent: l’esponente a cui elevare la base.

Utilizzare, poi, la funzione per calcolare:

    3⁴, ovvero 3 elevato alla potenza di 4. 
    43 , ovvero 4 elevato alla potenza di 3.
    25, ovvero 2 elevato alla potenza di 5. 
    52, ovvero 5 elevato alla potenza di 2.
'''


def recursivePower(base:int,esponente:int):
    # se esponente è 0, base^0=1
    if esponente==0:
        return 1
    #se base è 0, 0^n -0, così è possibile che torni 0 senza  calcolare 0^n per qualunque valore di n
    elif base==0:
        return 0
    #altrimenti calcola recursive power
    else:
        return int(base*recursivePower(base,esponente - 1))
#3⁴, ovvero 3 elevato alla potenza di 4.
risultato=recursivePower(3,4)
print(risultato)
#4 elevato alla potenza di 3
risultato1=recursivePower(4,3)
print(risultato1)
#2 elevato alla potenza di 5.
risultato2= recursivePower(2,5)
print(risultato2)
#5 elevato alla potenza di 2.
risultato3= recursivePower(5,2)
print(risultato3)

#oppure meglio ancora:
print(f"3^4:{recursivePower(3,4)}")
print(f"4^3:{recursivePower(4,3)}")
'''3^4=3*3^3=
=3*(3*3^2)=
3*(3*(3*3^1))
=3*(3*(3*(3*3^0)))
=3*(3*(3*(3*1)))
=27*3=81'''


'''0->3^0? ->3^0=1'''