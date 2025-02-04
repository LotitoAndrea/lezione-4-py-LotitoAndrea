litri = float(input("Inserisci il numero di litri di carburante da mettere: "))
costoLitro = 1.76
sconto = 0.05
totale = litri * costoLitro
if totale > 60:
    print("Totale prima dello sconto: ", totale)
    totale -= sconto * totale
    totale = round(totale, 2)
print("Totale da pagare: ", totale)