'''Make a class called User. Create two attributes called first_name and last_name, 
and then create several other attributes that are typically stored in a user profile. 
Make a method called describe_user() that prints a summary of the user’s information. 
Make another method called greet_user() that prints a personalized greeting to the user. 
Create several instances representing different users, and call both methods for each user.'''

class User:
    def __init__(self, first_name:str,last_name:str):
        self.first_name = first_name    
        self.last_name = last_name

    def describe_user(self):
        print(f"name: {self.first_name}, last name: {self.last_name}")
    
    def greet_user(self):
        print(f"It's a pleasure to have you here {self.first_name} {self.last_name}")

user1:User=User("Valentina","Bologna")
user2:User=User("Stefano","Martelloni")


user1.greet_user()
user2.greet_user()
user1.describe_user()
user2.describe_user()