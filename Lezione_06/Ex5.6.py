'''Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is a baby.
• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder.'''

#define Any
from typing import Any
variable_age:Any=int(input("What's the person's age?: "))

#if-elif-else chain that determines a person’s stage of life
if variable_age <2:
    print("The person is a baby")
elif variable_age>2 and variable_age<4:
    print("The person is a toddler")
elif variable_age>4 and variable_age<13:
    print("The person is a kid")
elif variable_age>13 and variable_age<20:
    print("the person is a teenager")
elif variable_age>20 and variable_age<65:
    print("the person is an adult")
else:
    print("the person is an elder")
