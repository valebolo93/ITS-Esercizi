import re
#inizio stringa
text:str = "Rome Paris"
result = re.match(r'[A-Z][a-z]+', text)
print(result.group())

#restituisce una lista Python di stringhe che contiene tutte le corrispondenze nell’ordine in cui sono state trovate
text:str = "I have 20 cats and 3 dogs"
numbers:list[str] = re.findall(r'\d+', text)
print(numbers)

#ogni gruppo è accessibile per indicizzazione. La posizione 0 è quella completa di default. La posizione 1 è la prima, la 2 è la seconda.
text:str = "Il codice è: 123-ABC"
match = re.search(r"(\d+)-([A-Z]+)", text)
if match:
    print("Intera corrispondenza:", match.group(0)) # Output: "123-ABC"
    print("Gruppo 1 (numeri):", match.group(1)) # Output: "123"
    print("Gruppo 2 (lettere):", match.group(2)) # Output: "ABC"

#sostituzione di un gruppo
text:str = "123-ABC"
new_text:str = re.sub(r"(\d+)-([A-Z]+)", r"\2-\1", text)
print(new_text) # Output: "ABC-123"

#non capturing
text:str = "abcabcabc"
print("Cattura:", re.findall(r"(abc)+", text)) # Output ['abc']
print("Non cattura:", re.findall(r"(?:abc)+", text)) # Output ['abcabcabc’]

#sovrascrive tutte le corrispondenze con un testo a vostra scelta
#Il testo con cui sostituire le corrispondenze deve essere passato come secondo parametro di trasferimento. 
# Il terzo parametro di trasferimento della funzione è la stringa da cercare. Se volete sovrascrivere non tutte le corrispondenze, 
# ma soltanto un determinato numero, potete specificare come quarto parametro di trasferimento un numero che indichi quante corrispondenze 
# devono essere sostituite a partire dalla prima.

string = "python è un linguaggio fantastico"
regex = "\s"
risultato1 = re.sub(regex, "0", string)
print(risultato1)
risultato2 = re.sub(regex, "0", string, 2)
print(risultato2)

#divide una stringa in una lista. La stringa viene interrotta dopo ogni corrispondenza con un’espressione regolare
#. Se volete dividere solo in modo limitato, potete passare un numero come terzo parametro opzionale,
# che determina il numero massimo di divisioni

string = "python è un linguaggio fantastico"
regex = "\s"
risultato1 = re.split(regex, string)
print(risultato1)
risultato2 = re.split(regex, string, 1)
print(risultato2)

#cerca una corrispondenza in una stringa.A questo scopo riceve prima l’espressione regolare e poi, come secondo parametro, la stringa in cui eseguire la ricerca
#Se non viene trovata nessuna corrispondenza, la funzione restituisce il valore “None

string = "python è un linguaggio fantastico"
regex = "\s"
match = re.search(regex, string)
if match:
	print("RegEx trovata.")
else:
	print("RegEx non trovata.")
