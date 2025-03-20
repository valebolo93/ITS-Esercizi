class Persona:

    def __init__(self):
        self.name:str= " "
        self.last_name:str= " "
        self.age:int = 0

    def displayData(self)->None:
        print(f"Nome:{self.name}\nCognome:{self.last_name}\nEtà:{self.age}")

    #funzione che consenta di impostare il valore di self.name
    def setName(self,name:str)->None:
        self.name=name
    
    #funzione che consenta di impostare un valore di un attributo self.last_name

    def setlastname(self,last_name:str)->None:
        self.last_name=last_name

    def setage(self,age:int)->None:
        self.age:int=age
        