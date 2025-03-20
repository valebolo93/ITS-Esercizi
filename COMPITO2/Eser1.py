'''Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit 
e viceversa a seconda del parametro to_fahrenheit. 
Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit.'''

def convert_temperature(to_fahrenheit:float=32.0) -> float:
    return ((celsius*9/5)+to_fahrenheit)
celsius=0

print(convert_temperature())

def convert_temperature(to_fahrenheit:float=32.0) -> float:
    return (to_fahrenheit- 32) * 5/9
print(convert_temperature())





