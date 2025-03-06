'''Write a function called describe_city() that accepts the name of a city and its country. 
The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. 
Call your function for three different cities, at least one of which is not in the default country.'''

def describe_city(city:str,country:str="Italy"):
    return f"{city} is in {country}"

#stampo il nome della città
print(describe_city("Roma"))
#stampo nome seconda città
print(describe_city("Firenze"))
#stampo nome città e paese diverso
print(describe_city("Paris","France"))