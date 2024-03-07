def calculator():

    print('Wybierz 1, aby policzyć pole prostokąta')
    print('Wybierz 2, aby policzyć pole kwadratu')
    print('Wybierz 3, aby policzyć pole trójkąta')
    print('Wybierz 4, aby policzyć pole trapezu')
    print('Wybierz 5, aby policzyć pole koła')

    num = int(input('Wybierz, co chcesz zrobić: '))

    if num == 1:
        a = int(input("Podaj 'a': "))
        b = int(input("Podaj 'b': "))
        return a * b
    elif num == 2:
        a = int(input("Podaj 'a': "))
        return a * a
    elif num == 3:
        a = int(input("Podaj 'a': "))
        h = int(input("Podaj 'h': "))
        return (a * h) / 2
    elif num == 4:
        a = int(input("Podaj 'a': "))
        b = int(input("Podaj 'b': "))
        h = int(input("Podaj 'h': "))
        return (a + b) * h / 2
    elif num == 5:
        r = int(input("Podaj 'r': "))
        return 3.14 * r ** 2
    else:
        print('Niepoprawny wybór. Spróbuj ponownie.')


wynik = calculator()
print('Wynik: ', wynik)
