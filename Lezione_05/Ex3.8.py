'''3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.'''

my_list_places:list[str]= ["Japan", "Australia", "Island", "Peru", "Egypt"]
print(my_list_places)
ordinata = sorted(my_list_places)
print(ordinata)
print(my_list_places)

ordinata = sorted(my_list_places, reverse=True)
print(ordinata)

ordinata = sorted(my_list_places, reverse=False)
print(ordinata)

ordinata = sorted(my_list_places)
print(my_list_places)


print("...............................................................................................................")
#modo alternativo in cui però c'è solo una lista e non due
my_list_places:list[str]= ["Japan", "Australia", "Island", "Peru", "Egypt"]
print(my_list_places)
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
my_list_places.sort()
print(my_list_places)
print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")

my_list_places.sort(reverse=True)
print(my_list_places)
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")