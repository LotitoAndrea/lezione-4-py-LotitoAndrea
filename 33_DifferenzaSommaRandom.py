import random
numero1 = random.randint(1, 10)
numero2 = random.randint(1, 10)
prodottoNumeri = numero1 * numero2
if prodottoNumeri < 20:
    risultato = numero1 - numero2
else:
    risultato = numero1 + numero2
print("numero1: ", numero1)
print("numero2: ", numero2)
print("prodottoNumeri: ", prodottoNumeri)
print("risultato: ", risultato)