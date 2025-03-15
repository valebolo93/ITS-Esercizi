'''An ice cream stand is a specific kind of restaurant. 
Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 
 or Exercise 9-4. Either version of the class will work; just pick the one you like better. 
 Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. 
Create an instance of IceCreamStand, and call this method. '''

class Restaurant:

    def __init__(self,restaurant_name:str,cuisin_type:str):
        self.restaurant_name=restaurant_name
        self.cuisin_type=cuisin_type


class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name:str,cuisin_type:str,flavors:list):
        super().__init__(restaurant_name,cuisin_type)
        self.flavors=flavors
        print(f"Gusti disponibili: {self.flavors}")
        

        
    def display_flavors(self):
        return self.flavors

icecream:IceCreamStand=IceCreamStand("Ice cream stand", "gelateria", ["Pistacchio","Fragola","Ciocciolato"])

icecream.display_flavors()

