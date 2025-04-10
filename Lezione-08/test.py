from persona_giusto import Persona
from studente import Studente

#creare un oggetto p di classe Persona

p:Persona = Persona("Valentina","Bologna",32)

#visualizza le info relative alla persona p

print(p)
#creare un oggetto studente1 di classe Studente
studente1:Studente = Studente("Stefano", "Martelloni",32,"0797434567")

#voglio controllare che studente sia istanza della classe studente

if isinstance(studente1,Studente):
    print("\nstudente1 è un oggetto della classe Studente")

#la funzione isinstance(obj,Class)->True se l'obj è un istanza della classe Class

#voglio sapere se studente1 è anche classe Persona visto che la classe Stud eredita dalla classe Persona

if isinstance(studente1, Persona):
      print("\nstudente1 è un'istanza della classe Persona")
else:
        print("\nstudente1 è  solo un'istanza della classe Studente e non della classe Persona")

#voglio controllare che l'oggetto p sia un'istanza di PErsona

if isinstance(p,Persona):
      print("\np è un'istanza della classe Persona")

    #voglio controllare che l'oggetto p sia un'istanza di Stud

if isinstance(p,Studente):
      print("\np è un'istanza della classe Persona e anche della classe Studente")
else:
      print("\np è solo un'istanza della classe Persona e non della classe Studente")
      
      #voglio controllare se la classe Studente è sottoclasse della classe Persona
    #issubclass(Class1,Class2)->controllare se Class1 è sottoclasse della Class2: -> in caso affermativo ritorna True

if issubclass(Studente,Persona):
      print("\nLa class Studente è sottoclasse della Class Persona")

print(studente1)
print("-------------------------------------------------")
print(p)

print(f"\nLa media dei voti degli esami sostenuti dallo studente 1 è pari a: {studente1.getMediaEsami([10,20,30])}")

#creiamo studente2

studente2: Studente = Studente(p.getName(),p.getLastName(),p.getAge(),"0456789")

print("-----------------------------------")
print(studente2)

#confrontare se studente1==p
print("\n",studente1==p)

#confronto studente 1 con studente 2
print("\n",studente1==studente2)

#verifichiamo che lo studente 1 sia uguare a se stesso
print("\n",studente1==studente1)

#modificare nome,cognome,età dello studente 2 affinchè abbia stesso nome,cognome ed età dello studente 1

studente2.setName(studente1.getName())
studente2.setLastName(studente1.getLastName())
studente2.setAge(studente1.getAge())

#provo di nuovo a confrontare studente1 e studente2
print("\n",studente1==studente2)
#ho forzato la matricola dello studente 2 ad essere uguale alla matricola dello studente1
studente2.setMatricola(studente1.getMatricola())
#confronto di nuovo studente1 constudente 2
print("\n",studente1==studente2)