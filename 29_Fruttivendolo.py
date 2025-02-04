prezzoPesche = float(input("inserisci il prezzo per una singola pesca "))
numeroPesche = int(input("inserisci il numero di pesche acquistate "))
totaleSpeso = prezzoPesche * numeroPesche
if totaleSpeso > 10:
    print("totale prima dello sconto: ", totaleSpeso)
    totaleSpeso -= 0.20 * totaleSpeso
    print("totale dopo lo sconto: ", totaleSpeso)
else:
    print("totale: ", totaleSpeso)
