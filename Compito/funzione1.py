

'''#def even_odd_pattern(numbers:list)-> list[int]:
    n_numbers:list=[]
    odd_numbers:list=[1,3,5,7,9]
    even_numbers:list=[2,4,6,8,10]
    if numbers %2==0:
            numbers.append(odd_numbers)
    if numbers %2!=0:
           numbers.append(even_numbers)
    return numbers

print(even_odd_pattern(n_numbe))''''''
'''




def even_odd_pattern(numbers:list)-> list[int]:
    new_numbers:list = []

    # Prima aggiungiamo tutti i numeri pari
    for numero in numbers:
        if numero % 2 == 0:
            new_numbers.append(numero)

    # Poi aggiungiamo tutti i numeri dispari
    for numero in numbers:
        if numero % 2 != 0:
           new_numbers.append(numero)

    return new_numbers