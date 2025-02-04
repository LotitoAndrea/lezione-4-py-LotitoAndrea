prezzo = float(input("inserisci il prezzo del biglietto "))
numero = int(input("inserisci il numero di biglietti acquistati "))
if 20 <= numero <= 40:
    numero -= 1
elif 40 < numero <= 60:
    numero -= 2
elif 60 < numero <= 80:
    numero -= 3
elif 80 <= numero <= 100:
    numero -= 4
elif numero > 100:
    numero -= 5
totale = numero * prezzo
print("il totale da pagare è", totale)