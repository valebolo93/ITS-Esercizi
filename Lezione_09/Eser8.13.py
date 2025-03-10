'''Build a profile of yourself by calling build_profile(), using your first and last names and three other
 key-value pairs that describe you. All the values must be passed to the function as parameters. 
The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"'''

def buid_profile(name:str,surname:str,age:int,colour_hair:str,weight:int):
    return f"My name is {name} {surname},age {age},hair {colour_hair},weigh {weight}"

print(buid_profile("Valentina", "Bologna", 32, "brown", 60))