'''Below is the function display_student(name, age).
 Assign a new name show_tudent(name, age) to it and call it using the new name.'''

#la mia funzione principale
def display_student(name:str,age:int) ->None:
    return f"My name is {name} and I'm {age} years old"


#definisco la mia funzione
display_student("Valentina",32)

#do un nuovo nome alla funzione
show_student=display_student

#stampo la nuova funzione sostituendola a display_student
print(show_student("Valentina",32))

