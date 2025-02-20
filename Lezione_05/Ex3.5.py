'''3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, 
so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.'''

mylist:list[str]= ["Totti", "Berlinguer", "Ghandi"]

print("Ghandi is not available")

mylist:list[str]= ["Totti", "Berlinguer", "Ghandi",]
mylist.remove("Ghandi")
print(mylist)
mylist.append("Giulio Cesare")
print(mylist)

print(f"I would like to invite you to dinner {mylist[0]}")
print(f"I would like to invite you to dinner {mylist[1]}")
print(f"I would like to invite you to dinner {mylist[2]}")