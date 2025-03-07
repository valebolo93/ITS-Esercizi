'''Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title.
 Once you have that information, 
call make_album() with the user’s input and print the dictionary that’s created. 
Be sure to include a quit value in the while loop.'''


while True:
    insert_album:str=input("Inserisci un album: ")
    insert_artist:str=input("Inserire nome artista: ")
    break
def make_album(album:str, artist:str, num_songs:int=None) ->dict:
     if num_songs is None:
        num_songs= "Unknown"
        return {insert_album:album, insert_artist:artist, "num_songs":num_songs}
print(make_album(insert_artist,insert_album))
         