from persona_giusto import Persona

class Studente(Persona):
    
    def __init__(self,name:str,last_name:str,age:int,matricola:str):   #inizializzare un oggetto della classe Studente
        super().__init__(name,last_name,age) #inizializza la superclasse
    #inizializzazione della classe stud

        self.setMatricola(matricola)
    #metodi setter

    #metodi che ci consentono di impostare il valore dell'attributo self.matricola
    def setMatricola(self,matricola:str)->None:
        
        #controllare che stringa non sia vuota
        if matricola:
            self.matricola=matricola
        else:
            print("Errore! La matricola non può essere una stringa vuota")
    
    
    
    ''' 
    attributi ereditati dalla classe Persona
    self.name
    self.last_name
    self-age

    attributi classe Studente:
    self.matricola
    
    SOLO COSA DIDATTICA PER VERIFICARE
    def inheritanceTest(self):
        #verificare che la classe studente eredita tutti gli attributi della calsse Persona
        self.name
        self.last_name
        self.age

        #verificare che la classe studenti erediti tutti i metodi della classe Persona
        self.getName()
        self.getLastName()
        self.getAge()
'''

