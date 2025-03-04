'''Suppose that you need to find the sum of integers from 1 to 10, 20 to 37, and 35 to 49. Write a Python program that
compute these three different sums.'''

sum:int=0


for i in range(1,11):
    sum= sum+i
print(f"La somma è: {sum}")

sum:int=0

for i in range(20,38):
    sum=sum+i
print(f"la somma è:{sum}")

sum:int=0

for i in range(35,50):
    sum=sum+i
print(f"la somma è {sum}")


#modo con funzioni

def sumInRange(a:int, b:int):
    result:int = 0
    for i in range(a, b+1):
        result = result + i
    return result

print(f"Sum from 1 to 10 is {sumInRange(1,10)}")
print(f"Sum from 2 to 38 is {sumInRange(2,38)}")
print(f"Sum from 35 to 50 is {sumInRange(35,50)}")

#se salvo le variabili:
mysum= sumInRange(1,10)
