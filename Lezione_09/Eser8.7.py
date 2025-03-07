''' Write a function called make_album() that builds a dictionary describing a music album. 
The function should take in an artist name and an album title, and it should return a dictionary 
containing these two pieces of information. Use the function to make three dictionaries representing different albums. 
Print each return value to show that the  dictionaries are storing the album information correctly.
 Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
 If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
Make at least one new function call that includes the number of songs on an album.'''

'''def make_album(album:str, artist:str, num_songs=None)->dict:
    if num_songs is None:
        num_songs= "Unknown"
    return {"albums":album,"artista":artist} 
dizionario:dict= {"albums":"album", }
Solo=(make_album("Solo","Ultimo"))
Colpa_delle_favole=(make_album("Colpa delle favole","Ultimo"))
Chiave=(make_album("Chiave","Ultimo"))

print(Solo)
print(Colpa_delle_favole)
print(Chiave)

num_songs=None'''


def make_album(album:str, artist:str, num_songs:int=None) ->dict:
    if num_songs is None:
        num_songs= "Unknown"

    return {"album":album, "artista":artist, "num_songs":num_songs} 

print(make_album("chiave", "ultimo"))
print(make_album("solo", "ultimo"))
print(make_album("colpa_delle_favole", "ultimo", 12))


