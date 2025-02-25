'''Scrivere un programma in Python che chieda all'utente di inserire il 
proprio nome e il proprio genere (specificato con "m" per maschio o "f" per femmina) e utilizzi lo statement match 
per fornire una risposta adeguata da inserire in un documento di identita'.

- Se il valore di gender è "m", stampare il nome e il genere come Maschio.
- Se il valore di gender è "f", stampare il nome e il genere come Femmina.
- Se il valore di gender è diverso da "m" o "f", stampare un messaggio di errore, indicando che non è possibile generare un documento di identità.
Expected Output:
Inserire nome: Luca
Inserire gender. Digitare m per maschio e f per femmina: m
Nome: Luca
Gender: Maschio
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Inserire nome: Anna
Inserire gender. Digitare m per maschio e f per femmina: f
Nome: Anna
Gender: Femmina
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Inserire nome: Alex
Inserire gender. Digitare m per maschio e f per femmina: x
Mi dispiace Alex, non e' possibile procedere con la generazione di un documento di identità!'''

nome:str=(input("Inserisci il tuo nome: "))
gender:str=(input("Inserire 'm' per maschio e 'f' per femmina: "))

match gender:
   
    case "m":
        print(f"{nome}")
        print(f"{gender}:'Maschio'")
    case "f":
        print(f"{nome}")
        print(f"{gender}: Femmina'")
    case _:
        print("Errore")
