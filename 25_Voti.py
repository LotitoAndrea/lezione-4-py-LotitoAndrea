print("Come è andata la verifica?")
voto = float(input("Inserisci un voto da 0 a 10: "))
if voto > 6:
    print("Bene. Hai preso più della sufficienza!")
elif voto == 6:
    print("Voto sufficiente.")
else:
    print("Purtroppo il tuo voto è insufficiente.")