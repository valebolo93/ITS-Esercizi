'''Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed.'''

name:list=["admin","Vale","Stefano","Sofi","Mik"]

for i in name:
    if name[1:]:
        print(f"Hello {name[1]}, thank you for logging in again")
        print(f"Hello {name[2]}, thank you for logging in again")
        print(f"Hello {name[3]}, thank you for logging in again")
        print(f"Hello {name[4]}, thank you for logging in again")
        break
    elif name[0]:
        print(f"Hello {name[0]}  would you like to see a status report?")
        break
#creo duplicato lista
name1=name

name1.pop(0)
name1.pop(0)
name1.pop(0)
name1.pop(0)
name1.pop(0)
print(name1)      #lista vuota

if name1==name1:
    print("We need to find some users!")
    

