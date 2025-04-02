'''
    Create a function that defines a product with a name, price, and quantity.
     Create a function that manages the shopping cart, allowing the user to add, remove,
     and view products in the cart.
    The function should calculate the cart total and apply any discounts or taxes.
     Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.
'''

class Product:

    def __init__(self,name:str,price:float,quantity:float):
        self.name=name
        self.price=price
        self.quantity=quantity



    def product_name(self,variabile_sconto,taxes=22):
        self.taxes=taxes
        self.variabile_sconto=variabile_sconto
        tax_value = self.price * (taxes / 100)
        discount_value = self.price * tax_value * (variabile_sconto / 100)
        return f"Nome prodotto: {self.name},prezzo: {self.price},quantità: {self.quantity},sconto: {discount_value},tasse: {taxes}"

    def shopping_cart(self):
        total_price = self.price * self.quantity
        taxes = total_price * 0.22  
        return sum(value),taxes
    
    print(shopping_cart)

products:dict={}


while True:
    select:str=str(input(" Insert: Add,remove or view products: "))
    match select:
        case "add":
            insert:str=input("Which product would you like to insert? ")
            if insert=="apple":
                products["apple"]=1.99
            elif insert=="pineapple":
                products["pineapple"]=2.67
            elif insert=="pear":
                products["pear"]=0.45
            elif insert=="banana":
                products["banana"]=0.32
            elif insert=="tomatoes":
                products["tomatoes"]=0.87
        case "remove":
            remove:str=input("Which product would you like to remove?: ")
            removed_product= products.pop(remove)
        case "view":
            print(products)
        case _:
            exit:str=("Do you want to exit?: ")
            if exit=="yes":
                print(f"Totale:{value}")

    for key,value in products.items():
        print(value)

        