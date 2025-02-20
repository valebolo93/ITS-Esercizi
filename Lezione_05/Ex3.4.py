'''3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people 
you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.'''

mylist:list= ["Totti", "Berlinguer", "Ghandi"]

for invitati in mylist:
    print(f"sei invitato a cena {invitati}")


#esercizio alternativo
mylist2:list[str]= ["Totti","Berlinguer","Ghandi"]
print(f"I would like to invite you to dinner {mylist2[0]}")
print(f"I would like to invite you to dinner {mylist2[1]}")
print(f"I would like to invite you to dinner {mylist2[2]}")