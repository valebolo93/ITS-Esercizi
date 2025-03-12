'''Generate a Python list of all the even numbers between 4 to 30'''

#creo una lista vuota
lista:list=[]
#uso un ciclo for con il range 4,30
for num in range(4,30):
#se i numeri sono positivi allora li aggiungo alla lista e poi stampo la lista
    if num%2==0:        
        lista.append(num)
        print(lista)

#modo alternativo   
print((list(range(4,30,2))))