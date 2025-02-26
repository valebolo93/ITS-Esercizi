'''4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers.
 (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)'''


lista_numeri= list(range(1,1000001))

#modo 1
for i in range(1,1000001):
    print(i)

#modo 2 
for i in lista_numeri:
    print(i)