'''Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.'''

# funzione con messaggio default
def make_shirt(size:str = "L",message:str="I love Python")->str:
    return f"Making  a shirt size: {size} with the following message: {message} " 
#stampo il messaggio di default
print(make_shirt()) 
#stampo modificando solo la taglia e stesso messaggio default
print(make_shirt("M"))
#stampo nuova taglia e nuovo messaggio 
print(make_shirt("S","I love Java"))