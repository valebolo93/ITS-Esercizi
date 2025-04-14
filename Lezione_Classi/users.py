'''Create a module users.py containing three classes:

    User: stores first_name, last_name, username, and email; includes describe_user() and greet_user() methods.
    Privileges: holds a list of privileges and a method show_privileges() to display them.
    Admin: stores a User instance and a Privileges instance as attributes.

In a separate file main.py, import the classes, create a User and a Privileges instance, pass them to Admin, 
and call describe_user() and show_privileges() to verify everything works correctly.'''

class User:
    def __init__(self,first_name:str,last_name:str,username:str,email:str):
            self.first_name=first_name
            self.last_name=last_name
            self.username=username
            self.email=email

    def describe_user(self):
        print(f"I dati dell'utente sono: Nome:{self.first_name},\nCognome: {self.last_name}, \nUsername: {self.username}\nemail: {self.email}")
    
    def greet_users(self):
        print(f"Benvenuto/a  {self.username}")


class Privileges:

    def __init__(self,privileges:str):
        self.privileges=privileges
    

    def show_privileges(self)->str:
        for element in self.privileges:
            print(f"{element}")
    
    
class Admin:
    def __init__(self,user:User,privileges:Privileges):
        self.user=user
        self.privileges=privileges

    

    
        
        