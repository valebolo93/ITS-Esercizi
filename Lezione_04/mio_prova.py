def prodotto (a:int,b:int):
    result:int= a * b
    return result

myprodotto= prodotto(2,10)
print(myprodotto)
print(f" Il mio prodotto sarà: {prodotto(2,10)}")

def prova():
    x= 100*2
    return x

y= 200*prova()
print(f"Il tuo prodotto sarà con gigino: {y}")