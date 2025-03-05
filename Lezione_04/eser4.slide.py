'''Write a function check_each(), which takes a list of numbers as argument.
Using a for loop, iterate through the list.
For each number, print “bigger” if it’s bigger than 5, “smaller” if it’s smaller than 5, and “equal” if it’s equal to 5.'''

lista:list[int]=[1,2,3,4,5,6,7,8,9,10]

def check_each(lista:list):
    for i in lista:
        if i > 5:
            print(f"{i} è Maggiore di 5")
        elif i < 5:
            print(f"{i} è Minore di 5")
        else:
            print(f"{i} è Uguale a 5")


check_each(lista)
