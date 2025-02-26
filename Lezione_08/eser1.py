'''prendere in input dall'utente una stringa con lo spazio e stampare una stringa come 
la prima ma con la lettera di ogni parola maiuscola'''



frase:str=input("Inserire una stringa: ")
print(frase.title())

parole= frase.split()     #la funzione split divide ogni parola in una frase
result:list[str] = []

for parola in parole:
    p_in =parola[:-1]
    p_ultima=parola[-1]
   
    nuova=p_in+p_ultima.upper()
    result.append(nuova)

print(" ".join(result))   #da modo di concatenare le stringhe

