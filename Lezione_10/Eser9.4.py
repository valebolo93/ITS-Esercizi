'''Start with your program from Exercise 9-1. Add an attribute called number_served 
with a default value of 0. Create an instance called restaurant from this class. 
Print the number of customers the restaurant has served, and then change this value and print it again. 
Add a method called set_number_served() that lets you set the number of customers that have been served. 
Call this method with a new number and print the value again. Add a method called increment_number_served()
 that lets you increment the number of customers who’ve been served. Call this method with any number you 
 like that could represent 
how many customers were served in, say, a day of business. '''

class Restaurant:

    def __init__(self,restaurant_name:str,cuisin_type:str,number_served:int=0): #attributo
        self.restaurant_name=restaurant_name
        self.cuisin_type=cuisin_type
        self.number_served = number_served

    def set_number_saved(self):
        print(f" Numero persone servite: {self.number_served}")
    
    def increment_number_served(self):


restaurant:Restaurant = Restaurant("Da Gigi","Romana")

restaurant.set_number_saved()