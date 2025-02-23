'''Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, e 
calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.

Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.'''

n1:int=int(input("Inserire un numero: "))
n2:int=int(input("Inserire un numero: "))
prodotto=1 

for i in range(min(n1,n2),max(n1,n2)+1):
    prodotto*=i
    
print(f"Il prodotto dei numeri compresi tra {n1} e {n2} è {prodotto}")

    


