def procent_tortu():
    try:
        gaste = int(input("Ilu masz gości?"))
        if gaste > 0:
            wynik = 100 / gaste
            print(f"Każdy z gości dostaje {wynik} procent tortu")
        else:
            print("Nikt cie nie odwiedził")
    except ValueError:
        print("Musisz podać liczbę gośći")


procent_tortu()
