'''Add an attribute called login_attempts to your User class from Exercise 9-3. 
Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
Make an instance of the User class and call increment_login_attempts() several times. 
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
Print login_attempts again to make sure it was reset to 0.'''

from typing import Any

#creazione classe
class User:
   
    def __init__(self, first_name:str,last_name:str,login_attempts:int):
        self.first_name = first_name    
        self.last_name = last_name
        self.login_attempts = login_attempts
        print(f"Login attempts: {login_attempts}")

    #creazione metodo
    def increment_login_attempts(self):
        new = self.login_attempts + 1     
        print(f"L'incremento dei login è pari a: {new}")
        return new

    #creazione altro metodo
    def reset_login_attempts(self):
        login_attempts = 0 
        print(f"Il reset è pari a : {login_attempts}")
    
    #creazione istanza
incr:User=User ("Valentina","Bologna",20)

incr.increment_login_attempts()
incr.reset_login_attempts()


