class Persona:

    def __init__(self,nome:str,cognome:str,data_di_nascita:str,**kwargs):

        self.nome = nome
        self.cognome = cognome
        self.data_di_nascita = data_di_nascita
        self.parametri_aggiuntivi = kwargs

    def codice_fiscale(self):
        return f"{self.nome},{self.cognome},{self.data_di_nascita}"


persona_1: Persona = Persona(nome= "Valentina", cognome= "Bologna", data_di_nascita="15/01/1993" )

print(persona_1.nome)
print(persona_1.cognome)
print(persona_1.data_di_nascita)

class Studente(Persona):
    
    def __init__(self,nome,cognome,data_di_nascita,corso_seguito,**kwargs):
        super().__init__(nome,cognome,data_di_nascita,**kwargs)

        self.corso_seguito = corso_seguito

studente1:Studente = Studente(nome="Stefano",cognome="Martelloni",data_di_nascita="30/06/1990",corso_seguito= "informatica")

print(persona_1.codice_fiscale())