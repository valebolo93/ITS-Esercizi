'''
    Create a function that generates a random number within a range specified by the user.
    Prompt the user to guess the number within a specified maximum number of attempts.
    Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
    Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.'''

import random

def generatore(a:int=1, b:int=20)->int:
    num_randomico= random.randint(a,b)
    i=5
    while i>0:
        tentativi=int(input(f"Indovina numero tra {a} e {b} in {i} tentativi: "))

        if tentativi<num_randomico:
            print("Numero troppo basso")
        elif tentativi >num_randomico:
            print("Numero troppo alto")
           
        else:
            print("Numero corretto")
            break
        i=i-1
#inizialmente non mi veniva perchè non richiamavo la funzione!
generatore()

            
       
            
