import re

text:str = "Rome Paris"
result = re.match(r'[A-Z][a-z]+', text)
print(result.group())


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