'''Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it.
 Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.'''

def make_shirt(size:str,message:str)->dict[str,str]:
    return {"sizes":size, "messages":message}


shirt= make_shirt("m","Forza Roma")
print(shirt[f"sizes"])
print(shirt["messages"])

print(shirt)