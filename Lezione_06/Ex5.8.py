'''Hello Admin: Make a list of five or more usernames, including the name 'admin'.
 Imagine you are writing code that will print a greeting to each user after they log in to a website.
Loop through the list, and print a greeting to each user.
• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.'''

name:list=["admin","Vale","Stefano","Sofi","Mik"]

for i in name:
        print(f"Hello {name[1]}, thank you for logging in again")
        print(f"Hello {name[2]}, thank you for logging in again")
        print(f"Hello {name[3]}, thank you for logging in again")
        print(f"Hello {name[4]}, thank you for logging in again")
        print(f"Hello {name[0]}  would you like to see a status report?")
        break
   