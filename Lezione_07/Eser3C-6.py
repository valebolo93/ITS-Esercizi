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

mammiferi=["cane", 
           "gatto",
           "cavallo",
           "elefante",
           "leone",
           "delfino",
           "balena"]
rettili=["serpente",
         "lucertola",
         "tartaruga",
         "coccodrillo"]
uccelli=["aquila",
         "pappagallo",
         "gufo",
         "falco",
           "gallina",
           "tacchino",
           "anatra"]
pesci=["squalo",
       "trota",
       "salmone",
       "carpa"]
animali:str = input("Inserire il nome di un animale: ")
habitat:str=input("Inserire l'habitat tra acqua,aria e terra: ")
habitat_type:list=["acqua",
                   "terra",
                   "aria"]
habitat_acqua:list=["tartaruga", "coccodrillo","squalo","trota","salmone","carpa","delfino","balena","cigno","anatra"]
habitat_terra:list=["cane","gatto","cavallo","elefante","leone","serpente","lucertola","gallina","tartaruga","anatra","cigno"]
habitat_cielo:list=["aquila","pappagallo","gufo","falco"]
unkwown_habitat:list=[]



match animali:
   
    case ("cane"|"gatto"|"cavallo"|"elefante"|"leone"|"balena"|"delfino"):
        print("Mammiferi")
        animal_type = "Mammiferi"
        
    case ("serpente"|"lucertola"|"tartaruga"|"coccodrillo"):
        print("Rettili")
        animal_type = "Rettili"
    case ["aquila"|"pappagallo"|"gufo"|"falco"|"gallina"|"tacchino"|"anatra"]:
        print("Uccelli")
        animal_type = "Uccelli"
    case ["squalo"|"trota"|"salmone"|"carpa"]:
        print("Pesci")
        animal_type= "Pesci"
    case _:
        print("Non so in quale categoria classificare ")

if animali in mammiferi and animali in habitat_terra:
    print(f"{animali} può vivere nell'habitat terra")
elif animali in mammiferi and animali in habitat_acqua:
    print(f"{animali} può vivere nell'habitat acqua")
elif animali in rettili and animali in habitat_terra:
    print(f"{animali} vive in habitat terra")
elif animali in rettili and animali in habitat_acqua:
    print(f"{animali} vive in habitat terra e habitat acqua")
elif animali in rettili and animali in habitat_terra:
    print(f"{animali} vive in habitat terra e habitat acqua")
elif animali in uccelli and animali in habitat_cielo:
    print(f"{animali} vive in habitat cielo")
elif animali in uccelli and animali in habitat_acqua:
    print(f"{animali} vive in habitat cielo e habitat acqua")
elif animali in uccelli and animali in habitat_terra:
    print(f"{animali} vive in habitat cielo e habitat terra")
elif animali in pesci and animali in habitat_acqua:
    print(f"{animali} vive in habitat acqua")
else:
    print(f"Animale o habitat non riconosciuti")





'''if animali not in mammiferi and animali not in rettili and animali not in uccelli and animali not in pesci:
    print("Errore")
    
if animali not in habitat_acqua and animali not in habitat_cielo and not habitat_terra:
    unkwown_habitat.append(habitat)
    print(unkwown_habitat)


if mammiferi in  habitat_terra:
    print(f"{animali} vive nell'habitat terra")
    
if rettili[0:2]in habitat_terra:
    print(f"{animali} vive nell'habitat terra")
elif rettili[2:3]:
    print(f"{animali} può vivere in habitat terra e acqua")
if uccelli in habitat_cielo:
        print(f"{animali} vive nell'habitat cielo")
else:
        print(f"{animali} non può vivere in questo habitat")'''
        
    
