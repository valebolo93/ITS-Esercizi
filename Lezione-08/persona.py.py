class Persona:
        

    def __init__(self):
        self.name:str=""
        self.last_name:str=""
        self.age:int=0

    def getname(self)->str:
        return self.name
    
    def getLastName(self)->str:
        return self.last_name
    
    def getAge(self)->str:
        return self.age
    
    def setAge(self,age:int)->int:
        self.age=age
        if age <0:
            print("l'età non può essere minore di 0")
            self.age=0
        elif age >130:
            print("L'età non può essere maggiore di 130 anni")
            self.age=130
        
    
    def setLastName(self,last_name:str)->str:
        self.last_name=last_name
    
    def setName(self,name:str)->str:
        self.name=name
    
    def __str__(self,name:str,last_name:str,age:int):
        return f"La persona: {self.name},{last_name} ha {age}anni"
    
    def __call__(self):
        print("Sei una persona")

individuo1:Persona=Persona("Valentina","Bologna","30")
        
        


