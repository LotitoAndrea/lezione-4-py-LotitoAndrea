consumo = float(input("Inserisci il consumo in metri cubi: "))
quotaFissa = 20.0
if consumo < 500:
    primoConsumo = consumo * 0.575
    secondoConsumo = 0
else:
    primoConsumo = 500 * 0.575 
    secondoConsumo = (consumo - 500) * 0.783
totale = quotaFissa + primoConsumo + secondoConsumo
print("Il totale da pagare è: ", totale)