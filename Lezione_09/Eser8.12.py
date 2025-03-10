'''Write a function that accepts a list of items a person wants on a sandwich. 
The function should have one parameter that collects as many items as the function call provides, 
and it should print a summary of the sandwich that’s being ordered.
 Call the function three times, using a different number of arguments each time.'''

lista=[]

def sandwich(a:str,b:str):
    return a,b



sandwich("Tomatoes","Salad")

primo_sandwich=sandwich("Bacon","salad")
secondo_sandwich=sandwich("Ketchup","Sausage")
terzo_sandwich=sandwich("Tomatoes","Salad")

print(f"Il primo panino ha i seguenti ingredienti:" + (str)(primo_sandwich))

print(f"Il primo panino ha i seguenti ingredienti:" + (str)(secondo_sandwich))

print(f"Il primo panino ha i seguenti ingredienti:" + (str)(terzo_sandwich))