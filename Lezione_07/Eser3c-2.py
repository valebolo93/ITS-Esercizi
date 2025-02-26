'''Esercizio 3C-2. Scrivere un programma in Python che converta un voto di laurea italiano (sistema in 110-emi) 
nel sistema GPA americano (scala 0-4).
Il programma deve accettare in input un voto di laurea compreso tra 66 e 110, espresso come numero intero e usare 
un match per determinare il corrispondente GPA americano, secondo questa tabella di conversione:

- 106-110 → 4.0
- 101-105 → 3.7
- 96-100 → 3.3
- 91-95 → 3.0
- 86-90 → 2.7
- 81-85 → 2.3
- 76-80 → 2.0
- 70-75 → 1.7
- 66-69 → 1.0
- Altro caso → "Voto non valido"

Expected Output:

Inserisci il voto di laurea: 110
Output: GPA 4.0'''

voto_laurea=input("Scrivere voto laurea: ")

if voto_laurea.isnumeric():
        voto_laurea=int(voto_laurea)
        match voto_laurea:
            case (106|107|109|109|110):
                print(f"Il voto di laurea {voto_laurea} corrisponderà ad un voto americano: 4.0")
            case (101|102|103|104|105):
                print(f"Il voto di laurea {voto_laurea} corrisponderà ad un voto americano: 3.7")
            case (96|97|98|99|100):
                print(f"Il voto di laurea {voto_laurea} corrisponderà ad un voto americano: 3.3")
            case (91|92|93|94|95):
                print(f"Il voto di laurea {voto_laurea} corrisponderà ad un voto americano: 3.0")
            case (86|87|88|89|90):
                print(f"Il voto di laurea {voto_laurea} corrisponderà ad un voto americano: 2.7")
            case (81|82|83|84|85):
                print(f"Il voto di laurea {voto_laurea} corrisponderà ad un voto americano: 2.3")
            case (76|77|78|79|80):
                print(f"Il voto di laurea {voto_laurea} corrisponderà ad un voto americano: 2.0")
            case (70|71|72|73|74|75):
                print(f"Il voto di laurea {voto_laurea} corrisponderà ad un voto americano: 1.7")
            case (66|67|68|69):
                print(f"Il voto di laurea {voto_laurea} corrisponderà ad un voto americano: 1.0")
            case _:
                print("Voto non valido")