'''4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2
 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), 
and use a for loop to print out the value of each cube.'''

#modo 1 solo con ciclo for
for i in range(1,11):
    print(i**3)


#modo 2 con lista
lista:list=[1,2,3,4,5,6,7,8,9,10]
for i in lista:
    print(i**3)