'''3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.'''

mylist:list= ["Totti", "Berlinguer", "Ghandi",]
mylist.insert(0,"Giulio Cesare")
mylist.insert(2,"Tonio Cartonio")
mylist.append("Leopardi")

print(mylist)

for invitati in mylist:
    print(f"We have a bigger table, so you're invited {invitati}")