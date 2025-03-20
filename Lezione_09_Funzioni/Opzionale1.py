'''Create a function that takes a student's name and their scores in different subjects as input.
The function calculates the average score and prints the student's name, average, and a message 
indicating whether the student passed the exam (average >= 60) or failed.
Create a for loop to iterate over a list of students and scores, calling the function for each student.'''


def student(myname:str, scores:list)-> None:
    media:float= sum(scores)/len(scores)
    if media >=60:
         print(f"{myname}, il tuo punteggio: {media:.2f}. Hai passato l'esame!")
    else:
        print(f"{myname}, il tuo punteggio è: {media:.2f}. Mi spiace, non hai passato l'esame!")

voti_studenti:list= [
("Stefano",[80,60,80]),
("Giacomo",[50,70,90]),
("Sofia",[76,84,67]),
("Martina",[86,90,76]),
("Daniele",[45,56,43])
]

for studenti in voti_studenti:
   names, scores = studenti
   student(names,scores)
