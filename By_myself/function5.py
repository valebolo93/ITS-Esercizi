'''    Create an outer function that will accept two parameters, a and b
    Create an inner function inside an outer function that will calculate the addition of a and b
    At last, an outer function will add 5 into addition and return it'''



def inner_function(a:int,b:int) -> int:
    return a+b
def outer_function(a:int,b:int) -> None:
    return (a+b)+5

print(inner_function(2,2))
print(outer_function(2,2))