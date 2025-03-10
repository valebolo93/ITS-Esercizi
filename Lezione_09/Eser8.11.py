'''Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages.
 After calling the function, print both of your lists to show that the original list has retained its messages.'''

lista:list=["Come va?",
            "Ti voglio bene",
            "Forza Roma",
            "W l'estate"]

lista1=lista[::]

print(lista)
print(lista1)