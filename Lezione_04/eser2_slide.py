'''Write a function check_length(), which takes a string as an argument.
Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters.'''

def check_length(puzzone):

    if len(puzzone) > 10:
        print(f"bigger then 10 characters")
    elif len(puzzone) < 10:
        print(f"smaller then 10 characters")
    else:
        print("uguale a 10")
    
check_length("puzzone")