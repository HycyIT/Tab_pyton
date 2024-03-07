def podaj_całkowita():
    try:
        num = int(input("Podaj liczbę całkowitą : "))
        print(f"{num} to liczba całkowita")
    except ValueError:
        print("Wprowadzona liczba nie jest liczba całkowitą")


podaj_całkowita()
