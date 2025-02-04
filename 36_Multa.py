velocita = float(input("Inserisci la velocità: "))
limiteVelocita = float(input("Inserisci il limite di velocità: "))
multa = 0
eccessoVelocita = velocita - limiteVelocita
if eccessoVelocita <= 0:
    print("Non hai superato il limite di velocità")
elif eccessoVelocita <= 10:
    multa = 36
elif 10 > eccessoVelocita <= 40:
    multa = 148
elif 40 > eccessoVelocita <= 60:
    multa = 370
else:
    multa = 500
print("La multa da pagare è di", multa, "euro")