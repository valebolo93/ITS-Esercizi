'''Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, entrambe contenenti valori interi, 
calcoli la somma incrociata degli elementi.

Esempio:

a[1] + b[n-1], a[2] + b[n-2], ...

Memorizzare ogni somma incrociata in una nuova lista c e, quindi, visualizzare in output le liste a, b, c.'''

#creazione delle due liste della stessa lunghezza e di numeri interi
lista_a:list[int]=[2,22,42,62,92]
lista_b:list[int]=[5,25,45,65,95]

#creo una terza lista per memorizzare le somme 
lista_c:list[int]=[]

#ho utilizzato il ciclo for col range per accedere alle liste con l'indice e sommarle con la funzione append nella terza lista
for i in range(len(lista_a)):
    lista_c.append(lista_a[i]+lista_b[i])

print(f"Lista a: {lista_a}")
print(f"Lista b: {lista_b}")
print(f"Lista c: {lista_c}")

               