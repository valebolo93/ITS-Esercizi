class Persona:
    '''Di una persona voglio sapere delle informazioni.
    Queste info vengono chiamare attributi(della classe Persona)
    Le info saranno:
    -nome,cognome,età.
    Come li rappresento?
    self.name:str(attributo di tipo stringa)
    self.lastname:str(attributo di tipo stringa)
    self.age:int(attributo di tipo int)'''

    #costruttore
    def __init__(self,name:str,last_name:str,age:int): #self significa che mi riferisco alla classe Persona
        self.name:str=name
        self.last_name:str=last_name
        self.age:int=age
        
    #funzione che mostri in output i dati relativi ad una persona

    def displayData(self)->None:
        print(f"Nome:{self.name},\nCognome:{self.last_name},\nEtà:{self.age}")
    