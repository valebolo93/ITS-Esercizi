import re
'Esercizio 1'
def is_integer(num:int)->bool:
    #se il numero è intero ritorna True,altrimenti False
    if num%1==0:
        return True
    else:
        return False

print(is_integer(4))
print(is_integer(-4))
print(is_integer(-4.2))

'Esercizio 2'

def extract_emails(text:str)->list:
    #regex creata per email
    regex = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}'
    new:str= re.findall(regex,text)
    return new
    
text:str = "Contattaci a info@azienda.com oppure support@help.org"
result = extract_emails(text)
print(result)

'Esercizio 3'

def mask_numbers(test:str):
    #regex dei numeri
    regex:str= r'[0-9]+'
    #sostituisce i numeri con l'asterisco
    new:str=re.sub(regex,"###",text)
    return new

text:str = "Il codice è 12345 e la data è 2025."
risultato=mask_numbers(text)
print(risultato)

'Esercizio 4'

def is_valid_cap(cap:str)->bool:
    regex:int=r'^\d{5}$'
    return bool (re.fullmatch(regex,cap))
print(is_valid_cap("70124"))
print(is_valid_cap("A0123"))

'Esercizio 5'
def find__dates(text:str):
    regex:str=r'\d{2}/\d{2}/\d{4}'
    date:str= re.findall(regex, text)
    return date

text:str= "Le date importanti sono 09/04/2025 e 15/08/2023."
result=(find__dates(text))
print(result)

'Esercizio 6'

def check_product_code(code:str)->bool:
    regex:str= r'^[A-Z]{4}-\d{4}-[A-Z]{2}$'
    return bool (re.fullmatch(regex,code))
print(check_product_code("PROD-9876-ZX"))
print(check_product_code("PROD-98-ZX"))

'Esercizio 7'

def find_codes(text:str)->bool:
    regex:str= r'^[A-Z][a-z]{2,}'
    return bool (re.fullmatch(regex,text))

print(find_codes("Valentina"))
print(find_codes("valentina"))

'Esercizio 8'

def find_fc(text:str)->str:
    regex:str= r'[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}'
    return re.findall(regex,text)

testo:str="Mario Rossi CF: RSSMRA85M01H501Z, mentre Maria Bianchi ha il CF BNCMRA85T41H501Y."
print(find_fc(testo))