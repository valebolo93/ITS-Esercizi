'''3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have 
space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, 
print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an 
empty list at the end of your program.'''

mylist:list= ["Totti", "Berlinguer", "Ghandi",]
print(mylist)

mylist.insert(0,"Giulio Cesare")
mylist.insert(2,"Tonio Cartonio")
mylist.append("Leopardi")
print(mylist)

print("..........................................................")
print(f"you're invited to the Party {mylist[0]}")
print(f"you're invited to the Party {mylist[1]}")
print(f"you're invited to the Party {mylist[2]}")
print(f"you're invited to the Party {mylist[3]}")
print(f"you're invited to the Party {mylist[4]}")
print(f"you're invited to the Party {mylist[5]}")

print("'''''''''''''''''''''''''''''''''''''''''''''''''")

mylist2:list[str]= ["Giulio Cesare", "Totti","Tonio Cartonio","Berlinguer", "Ghandi","Leopardi"]
print(mylist2)


print("You can invite just 2 people")

print(f"I'm sorry {mylist2[2]} but i can't invite you anymore!")
mylist2.pop(2)

print(f"I'm sorry {mylist2[3]} but i can't invite you anymore!")
mylist2.pop(3)

print(f"I'm sorry {mylist2[0]} but i can't invite you anymore!")
mylist2.pop(0)

print(f"I'm sorry {mylist2[1]} but i can't invite you anymore!")
mylist2.pop(1)
print(mylist2)


print(f"{mylist2[0]} I confirm your invitation!")
print(f"{mylist2[1]} I confirm your invitation!")

print(mylist2)
mylist2:list= ["Totti","Leopardi"]

del mylist2[0]

print(mylist2)

del mylist2[0]
print(mylist2)






