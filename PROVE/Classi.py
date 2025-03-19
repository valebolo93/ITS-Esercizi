'''Creare una classe Persona che abbia i seguenti attributi: 
nome, età, sesso. Aggiungi un metodo “presentati” che stampi una frase di presentazione della persona,
 ad esempio “Ciao, mi chiamo Marco e ho 32 anni”.'''

class Persona:
    def __init__(self,nome:str,età:int,sesso:str):
        self.nome=nome
        self.età=età
        self.sesso=sesso

    def presentation(self):
        print (f"Ciao, mi chiamo {self.nome}, ho {self.età} anni e sono {self.sesso} ")
    
persona1: Persona= Persona("Valentina",32, "femmina")

persona1.presentation()
