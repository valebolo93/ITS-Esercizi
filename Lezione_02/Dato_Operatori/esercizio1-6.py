#eser 1-6
ITS_Bakery_Menù:dict = {"Pizza":9.00, "Pasta":10.50, "Zuppa":7.00, "Hamburger": 15.50, "Cotoletta": 10.00, "Salmone": 20.20, "Patatine_Fritte": 5.50, "Patate_al_forno": 5.50, 
                        "Verdura_del_giorno": 7.00, "Cheesecake": 6.00, "Tiramisu": 6.00, "Focaccia_con_Nutella": 6.00, "Coca_Cola": 3.50, "Acqua": 1.50, "Vino": 5.00}

totale = 0
ordine:dict={"Pizza":9.00, "Patatine_Fritte": 5.50, "Cheesecake": 6.00, "Coca_Cola": 3.50}

totale += ordine["Pizza"]
totale += ordine["Patatine_Fritte"]
totale += ordine["Cheesecake"]
totale += ordine["Coca_Cola"]

print(totale)