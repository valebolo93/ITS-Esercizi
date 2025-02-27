'''Esercizio 3C-5. Scrivere un programma in Python che memorizzi il nome, il ruolo e l'età di un utente in un dizionario.
 Il nome, il ruolo e l'età devono essere inseriti in input dall'utente stesso. 
 Il programma deve determinare il livello di accesso ai servizi in base al ruolo e all'età dell'utente secondo questo schema:
- Admin → "Accesso completo a tutte le funzionalità."
- Moderatore → "Può gestire i contenuti ma non modificare le impostazioni."
- Utente adulto (età ≥ 18) → "Accesso standard a tutti i servizi."
- Utente minorenne (età < 18) → "Accesso limitato! Alcune funzionalità sono bloccate."
- Ospite → "Accesso ristretto! Solo visualizzazione dei contenuti."
- Ruolo non riconosciuto → "Attenzione! Ruolo non riconsciuto! Accesso Negato!"'''
#help(dict)

nome=input("Inserire il nome: ")
ruolo=input("Inserire il ruolo: ")
eta:int=int(input("Inserire eta: "))

dizionario:dict[any]={"nome":nome, "ruolo":ruolo, "eta":eta}

match dizionario:
    case {"nome":nome, "ruolo":"admin", "eta":eta}:
        print("Accesso completo a tutte le funzionalità.")
    case {"nome":nome, "ruolo":"moderatore", "eta":eta}:
        print(f"Salve {nome}! Può gestire i contenuti ma non modificare le impostazioni")
    case {"nome":nome, "ruolo":"utente", "eta":eta}:
        if eta >=18:
            print("Accesso standard a tutti i servizi")
        else:
            print("Accesso limitato! Alcune funzionalità sono bloccate")        
    case {"nome":nome, "ruolo":"ospite", "eta":eta}:
        print("Accesso completo a tutte le funzionalità.")
    case _:
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato")
    



