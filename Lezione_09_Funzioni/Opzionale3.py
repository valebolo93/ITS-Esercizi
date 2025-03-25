'''
    Create a function that defines a product with a name, price, and quantity.
     Create a function that manages the shopping cart, allowing the user to add, remove,
     and view products in the cart.
    The function should calculate the cart total and apply any discounts or taxes.
     Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.
'''
from typing import Any

def product_name(name:str,price:float,quantity:float)->str:
    return f"Nome prodotto: {name},prezzo: {price},quantità: {quantity}"

def shopping_cart():
    return [products]

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
            elif insert=="tomatoes":
                products["tomatoes"]=0.87
        case "remove":
            remove:str=input("Which product would you like to remove?: ")
            removed_product= products.pop[remove]
        case "view":
            print(products)