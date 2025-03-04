def substract(a:int,b:int):
    result:int = a-b
    return result


mysubstract= substract(10,5)
print(mysubstract)
print("---------------------------------------------------------------------")
#con input

x:int=int(input("Inserire numero: "))
g:int=int(input("Inserire numero: "))

def substract(x:int,g:int)->int:
    result:int = x - g
    return result

mysubstract1= substract(x,g)
print(mysubstract1)