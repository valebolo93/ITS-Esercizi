'''Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. 
Also, it must return both addition and subtraction in a single return call.'''

def calculation(a:int,b:int) -> int:
    return f"La somma è pari a {a+b}, la sottrazione è pari a {a-b}"

print(calculation(10,2))