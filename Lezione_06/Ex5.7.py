'''5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that 
check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, 
the if block should print a statement, 
such as You really like Apples!'''

favourite_fruits:list=["Strawberry","Pineapple","Peach"]
frutta:str=input("Write the name of a fruit: ")

if frutta in favourite_fruits:
    print("You really like Peach")
if frutta != favourite_fruits:
    print(f"You don't like {frutta}")

print("--------------------------------------------------------------------------------------------------------------")

if favourite_fruits== "Strawberry":
    print("You really like Strawberry!")
elif favourite_fruits== "Pineapple":
    print("You really like Pineapple!")
elif favourite_fruits== "Peach":
    print("You really like Peach!")
elif favourite_fruits=="Apple":
    print()
else:
    print()