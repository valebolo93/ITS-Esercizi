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
        if age<0 or age>130:
            self.age = 0
        else:
            self.age = age

    #funzione che consente d ritornare il valore di self.name

    def getName(self)->str:
        return self.name
    
    #funzione che consente di ritornare il valore di self.lastname

    def getlastname(self)->str:
        return self.last_name
    
    #funzione che consente di tornare il valore di self.age

    def getAge(self)->int:
        return self.age
