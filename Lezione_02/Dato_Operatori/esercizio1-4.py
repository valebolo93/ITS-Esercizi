#eser 1-4
x: int = 2025
mylist= [2,0,2,5]
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])

n=int(input("Inserisci un numero di 4 cifre"))
m = n //1000
c = n //100 - m * 10
d = n //10 - m * 100 - c * 10
u = n - m * 1000 - c * 100 - d * 10
print(m)
print(c)
print(d)
print(u)