'''dal file persona.py importa la classe Persona
from persona import Persona

#creo una persona

#creo istanza
vb:Persona=Persona("Valentina","Bologna",32)

print(vb.name,vb.last_name,vb.age)

#richiamare la funzione displayData della classe persona per mostrare in output i dati relativi alla persona vb

vb.displayData()

print("----------------------------------------")'''
#dal file persona2 importa la classe persona
from persona2 import Persona

vb:Persona=Persona()

#richiamo la funzione displayData della classe persona per mostrare in outpute le info relative all'oggetto vb

vb.displayData()

#modificare il nome della persona vb

vb.setName("Valentina")
print("----------------------------------------")

vb.displayData()

#modificare il cognome della persona vb

vb.setlastname("Bologna")
print("----------------------------------------")

vb.displayData()

#modificare età della persona vb

vb.setage(32)
print("----------------------------------------")

vb.displayData()
