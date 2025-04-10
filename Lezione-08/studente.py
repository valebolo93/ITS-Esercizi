from persona_giusto import Persona
from typing import Any

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

    def getMatricola(self)->str:
        return self.matricola

        #metodo che consente di visualizzare le info relative all'oggetto della classe.
        #overwriting
    def __str__(self):
        return f"\nNome: {self.getName()}\nCognome:{self.getLastName()}\nMatricola: {self.getMatricola()}"

        #metodo che consente di calcolare la media degli esami sostenuti da uno studente

    def getMediaEsami(self,voti_esami:list[int])->float:
        #se la lista non è vuota
        if voti_esami:
            #calcolare la somma dei voti
            somma:int=0
            for voto in voti_esami:
                somma+=voto

            #ritornare la media
            return round(somma/len(voti_esami),2)
            #se la vista è vuota
        else:
            return 0.00
        
        #definire un metodo che consente di confrontare gli oggetti della classe Studente e stabilere se questi due oggetti siano uguali o meno
    #due studenti sono uguali se hanno la stessa matricola
    def __eq__(self, other)-> bool:
        #Se other è None, oppure se other non è istanza della classe Studente, ritorna False

        if other is None or not isinstance(other,type(self)):
            return False
        #altrimenti valuta la seguente uguaglianza
        else:
            return self.getMatricola()==other.getMatricola()



    
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

