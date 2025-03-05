'''Write a function add_one(). It takes an integer as argument. The function adds 1 to the integer and returns it.
Write another function add_one_to_list(). It takes a list of integers as argument.
Define a variable new_list in this function.
Using a for loop, iterate through the argument list.
Using add_one(), fill new_list with integers from the argument list incremented
by 1.
Print new_list.
Example:
add_one_to_list([1, 2, 3])
>>> [2, 3, 4]'''

def add_one(a:int):
    a += 1
    return a

list:list=[1,2,3,4,5,6]

def add_one_to_list(list):
    new_list =[]

    for a in list:
        new_list.append(add_one(a))

    return new_list
print(add_one_to_list(list))

