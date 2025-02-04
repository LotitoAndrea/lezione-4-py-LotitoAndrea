annoNascita = int(input("Inserisci il tuo anno di nascita: "))
if annoNascita < 1946:
    print("prima dei boomers")
elif 1946 <= annoNascita <= 1964:
    print("boomer")
elif 1965 <= annoNascita <= 1980:
    print("generazione X")
elif 1981 <= annoNascita <= 2000:
    print("generazione Y, millennials")
elif annoNascita > 2000:
    print("generazione Z")