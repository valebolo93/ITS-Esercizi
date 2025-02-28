'''5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.'''

parole:str= input("Inserisci tipologia macchina,moto,occhiali,profumo,telefono:  ")
car:str= "Ferrari"

if parole=="Ferrari":
        print(f"I predict"+ car == "Ferrari")
else:
        
        print(f"I predict"+ car == 'audi')

'''moto:str= "Ducati"
print(f"Is moto== 'Ducati'? I predict True.")
print(moto == 'Ducati')
print("\nIs moto == 'Kawasaki'? I predict False.")
print(moto == 'Kawasaki')

profumo:str= "Lu Jo"
print(f"Is profumo== 'Lu Jo? I predict True.")
print(profumo == 'Lu Jo')
print("\nIs profumo== 'Lu Jo'? I predict False.")
print(profumo == 'D&G')

occhiali:str="Rayban"
print(f"Is occhiali== 'Rayban'? I predict True.")
print(occhiali == 'Guess')
print("\nIs occhiali == 'Guess'? I predict False.")
print(occhiali== 'Guess')

telefono:str="Iphone"
if telefono=="Iphone":
        print(f"I predict {telefono} it's True.")

print("\nIs telefono == 'Samsung'? I predict False.")
print(telefono== 'Samsung')



if parole in car is True:
        print(f"I predict {parole} it's True")

        
else:
        print(f"I predict {car} it's False")
        

if parole in moto:
        print(f"I predict {moto} it's True")
          
else:
        print(f"I predict {moto} it's False")
        

if parole in profumo:
        print(f"I predict {profumo} it's True")
           
else:
        print(f"I predict {profumo} it's False")

if parole in occhiali:
        
        print(f"I predict {occhiali} it's True")
           
else:
        print(f"I predict{occhiali} it's False")

if parole in telefono:
        print(f"I predict {telefono} it's True")
           
else:
        print(f"I predict {telefono} it's False")'''
        

