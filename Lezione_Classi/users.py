'''Create a module users.py containing three classes:

    User: stores first_name, last_name, username, and email; includes describe_user() and greet_user() methods.
    Privileges: holds a list of privileges and a method show_privileges() to display them.
    Admin: stores a User instance and a Privileges instance as attributes.

In a separate file main.py, import the classes, create a User and a Privileges instance, pass them to Admin, 
and call describe_user() and show_privileges() to verify everything works correctly.'''

class User:
    def __init__(self,firs_name:str,last_name:str,email:str):
            self.first_name=firs_name
            self.last_name=last_name
            self.email=email

    def describe_user(self):
        return f"I dati dell'utente sono: {self.first_name},n\{self.last_name}\n{self.email}"
    
    def greet_users(self):
        return f"Benvenuto/a {self.first_name},{self.last_name}{self.email}"
    


class Privileges:

    def __init__(self,lista_privilegi:list)->list:
        self.lista_privilegi=lista_privilegi
        lista_privilegi:list=["accesso diretto","visualizza file", "copia hard disk"]

    def show_privileges(lista_privilegi:list)->list:
        return lista_privilegi
    
impronta:Privileges=Privileges("impronta digitale")
    
class Admin(User,Privileges):
    def __init__(self,user:str,privileges:str):
        self.user=user
        self.privileges=privileges

    

    
        
        