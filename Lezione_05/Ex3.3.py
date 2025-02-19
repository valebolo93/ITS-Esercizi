'''Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”'''

mylist:list[str]= ["motorbike", "car", "plane"]

for mezzi in mylist:
    print(f"I would like to own a {mezzi}")
else:
    print(f"Finished")

#exercise
mylist2:list[str]= ["motorbike", "car", "plane"]
print(f"I would like to own a {mylist2[0]}")
print(f"I would like to own a {mylist2[1]}")
print(f"I would like to own a {mylist2[2]}")


