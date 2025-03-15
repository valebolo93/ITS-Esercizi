'''Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, 
and call describe_restaurant() for each instance.'''

class Restaurant:

    def __init__(self,restaurant_name:str,cuisin_type:str):
        self.restaurant_name=restaurant_name
        self.cuisin_type=cuisin_type

    def descrive_restaurant(self):
        print(f"{self.restaurant_name}: {self.cuisin_type}")
    
    def open_restaurant(self):
        print("The restaurant is open")

restaurant:Restaurant= Restaurant("Da Gigi","romana")
restaurant1:Restaurant= Restaurant("Marechiaro","pesce")
restaurant2:Restaurant= Restaurant("Pizzenfaccia","pizzeria")

print(restaurant.restaurant_name)
print(restaurant.cuisin_type)
print(restaurant1.restaurant_name)
print(restaurant1.cuisin_type)
print(restaurant2.restaurant_name)
print(restaurant2.cuisin_type)


restaurant.descrive_restaurant()
