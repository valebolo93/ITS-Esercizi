'''Il fattoriale di un intero non negativo n, scritto n!, è il prodotto

n * (n-1) * (n-2) * ... * 1

con 1! uguale a 1 e 0! definito come 1.
Si scriva una funzione ricorsiva recursiveFactorial che dato un numero n calcoli n!.'''
def recursiveFactorial(n:int):
    if n <0:
        print("Error")
        return 0
        
    elif n==0 or n==1:
        #0! e 1! tornano 1
        return 1
    else:
        #
        int(n*recursiveFactorial(n-1))










    '''5!=5*4*3*2*1
    5!=5*4!=5*4*3!=5*4*3*2!=5*4*3*2*1!=5*4*3*2*1=120'''