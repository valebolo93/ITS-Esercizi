'''Esercizio 3C-6. Modificare il codice dell'esercizio 3C-4, affinchè si possa scrivere un 
codice python che consenta all'utente di inserire il nome di un animale ed un habitat. 
Quando il codice dell'esercizo 3C-4 classifica l'animale inserito in una delle 
categorie tra mammiferi, rettili, uccelli o pesci, oltre a mostrare un messaggio a schermo,
 deve salvare tale categoria in una variabile animal_type. Se l'animale inserito 
 non è classificabile in una delle quattro categorie proposte, il valore di animal_type sarà ' "unknown".
Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.
Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.
Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.
Categorie di habitat:
- acqua
- aria
- terra
NOTA.
Il codice deve produrre un risultato sensato, ovvero che l'animale inserito possa effettivamente vivere nell'habitat specificato.
Tenere in considerazione il fatto che alcuni animali tra quelli specificati possono vivere in più di un habitat, mentre altri solo in uno.

Suggeirmento: può essere utile per coprire tutti i possibili casi implementare istruzioni match annidate.'''

animali:str = input("Inserire il nome di un animale: ")
habitat:str = input("Inserire habitat tra acqua, aria e terra: ")
animal_type:str= input("Inserire categoria animale tra mammiferi,rettili,uccelli e pesci: ")
dizionario:dict[any]= {"nome animale":animali,"categoria":animal_type, "habitat": habitat}
rettili:list= ["serpente", "lucertola", "tartaruga", "coccodrillo"]
mammiferi:list=["cane","gatto""cavallo","elefante","leone","balena","delfino"]
uccelli:list= ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
pesci:list=["squalo","trota","salmone","capra"]

match dizionario:
   
    case {"nome animale":animali,"categoria":animal_type, "habitat": habitat}:
            print("Mammiferi")
    case ("serpente"|"lucertola"|"tartaruga"|"coccodrillo"):
        print("Rettili")
    case ("aquila"|"pappagallo"|"gufo"|"falco"|"cigno"|"anatra"|"gallina"|"tacchino"):
        print("Uccelli")
    case ("squalo"|"trota"|"salmone"|"carpa"):
        print("Pesci")
    case _:
        print("Non so in quale categoria classificare ")