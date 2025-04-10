class Persona:
     
    def __init__(self,name:str,last_name:str,age:int):
        self.setName(name)
        self.setLastName(last_name)
        self.setAge(age)


#metodo peciale che torna una stringa e che viene chiamata automaticamente quando si usa l'istruzione
#print(obj), dove obj è un oggetto della classe persona
#funzione che mi mostri in output i dati relativi ad una persona

    def __str__(self)->str:
        return f"Nome: {self.name}\nCognome: {self.last_name}\nEtà:{self.age}"

    #il metodo _call__ mi consente di usare l'oggetto della Classe Persona istanziato come una funzione.
    #quindi un oggetto della classe Persona si comporta come una funzione

    def __call__(self):
        if self.age <18:
            print(f"{self.name}")

    #metodi setter

    def setName(self, name:str)->None:
        if name:
            self.name=name
        else:
            print("Error!")

    def setLastName(self, last_name:str)->None:
        if last_name:
            self.last_name=last_name
        else:
            print("Error!")

    def setAge(self, age:int)->None:
        if age <0 or age >130:
            self.age=0
        else:
            self.age=age

    #metodi getter

    def getName(self)->str:
            return self.name
        
    def getLastName(self)->str:
            return self.last_name
        
    def getAge(self)->str:
            return self.age
        