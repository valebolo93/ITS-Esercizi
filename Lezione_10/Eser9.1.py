'''Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes:
 a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that 
 prints these two pieces of information,and a method called open_restaurant() that prints a message
   indicating that the restaurant is open. Make an instance called restaurant from your class. 
Print the two attributes individually, and then call both methods.'''

class Restaurant:

    def __init__(self,restaurant_name:str,cuisin_type:str):
        self.restaurant_name=restaurant_name
        self.cuisin_type=cuisin_type

    def descrive_restaurant(self):
        print(f"{self.restaurant_name}: {self.cuisin_type}")

    

    def open_restairant(self):
        print("The restaurant is open")

restaurant:Restaurant= Restaurant("Da Gigi","romana")

print(restaurant.restaurant_name)
print(restaurant.cuisin_type)

restaurant.descrive_restaurant()
restaurant.open_restairant()
