'''Exercise 1
Write a function check_value(), which takes a number as an argument.
Using if / else, the function should print whether the number is bigger, smaller, or equal to 5'''

def check_value(a:int):
    if a>5:
        print("Maggiore di 5")
    elif a<5:
        print("Minore di 5")
    else:
        print("Uguale a 5")
    
check_value(6)