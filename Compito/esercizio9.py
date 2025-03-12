'''Il valore di π può essere approssimato utilizzando la seguente serie infinita:

π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

Scrivere un programma che calcoli il valore di π utilizzando questa serie e determini quanti termini sono necessari 
per ottenere approssimazioni sempre più accurate. Quindi:

progettare un algoritmo che mostri in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.141;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.1415;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14159.
Nota: Il programma deve iterare fino a raggiungere ciascuna delle soglie indicate, contando il numero di termini necessari.'''

def computePI(approximation_value:float,decimal_digits) -> int:

    terms:int=0
    pi:float=0
    i:int=0

    while round(pi,decimal_digits) !=approximation_value:

        if i%2==0:
            pi = pi +4/(2*i +1)

        else:
            pi = pi -4/(2*i+1)

        terms = terms + 1

        i = i + 1

    return terms

# calling computePI function to determine how many terms are needed to obtain 3.14 ( 152 terms)
print(f"{computePI(3.14, 2)} terms are needed to compute a value of pi approximated to 3.14!")
# calling computePI function to determine how many terms are needed to obtain 3.141 ( 916 terms)
print(f"{computePI(3.141, 3)} terms are needed to compute a value of pi approximated to 3.141!")
# calling computePI function to determine how many terms are needed to obtain 3.145 ( 7010 terms)
print(f"{computePI(3.1415, 4)} terms are needed to compute a value of pi approximated to 3.1415!")
# calling computePI function to determine how many terms are needed to obtain 3.1459 ( 130'658 terms)
print(f"{computePI(3.14159, 5)} terms are needed to compute a value of pi approximated to 3.14159!")