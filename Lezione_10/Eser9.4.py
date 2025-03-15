'''Inizia con il tuo programma dall'esercizio 9-1. Aggiungere un attributo chiamato numero-servito 
con un valore predefinito di 0. Crea un'istanza chiamata ristorante di questa classe.
 Stampa il numero di clienti che il ristorante ha servito, quindi cambia questo valore e stampalo di nuovo. 
 Aggiungere un metodo chiamato set-number-served() che consente di impostare il numero di clienti che sono stati serviti. 
 Chiama questo metodo con un nuovo numero e stampa nuovamente il valore.
Aggiungere un metodo chiamato incremento-number-served() che consente di aumentare il 
numero di clienti che sono stati serviti. Chiama questo metodo con qualsiasi numero che 
ti piace potrebbe rappresentare quanti clienti sono stati serviti,
 ad esempio, in un giorno di lavoro.'''

class Restaurant:

    def __init__(self,restaurant_name:str,cuisin_type:str,number_served:int=0): #attributo
        self.restaurant_name=restaurant_name
        self.cuisin_type=cuisin_type
        self.number_served = number_served
        self.numberserved1 = 50
        self.numberserved2=70
        print(f"Inizialmente il numero di persone servite è: {self.number_served}")

    def set_number_saved(self):
        print(f"Nel corso della giornata il numero persone servite è: {self.numberserved1}")


        
    def increment_number_served(self):
        print(f"A fine giornata i clienti serviti sono: {self.numberserved2}" )       

restaurant:Restaurant = Restaurant("Da Gigi","Romana",20)



restaurant.set_number_saved()
restaurant.increment_number_served()
