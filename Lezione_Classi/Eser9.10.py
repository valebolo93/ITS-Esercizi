'''Using your latest Restaurant class, store it in a module.
 Make a separate file that imports Restaurant. Make a Restaurant instance, 
 and call one of Restaurant’s methods to show that the import 
 statement is working properly.'''

from Restaurant_9_2 import Restaurant

nome_ristorante:Restaurant=Restaurant("Da Cesare","Cucina Romana")

nome_ristorante.open_restaurant()
