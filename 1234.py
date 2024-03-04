definitions = {}

while True:
    print("Wybierz '1', aby dodać nową definicję")
    print("Wybierz '2', aby wyszukać definicję")
    print("Wybierz '3', aby usunąć definicję")
    print("Wybierz '4', aby pokazać słownik")
    print("Wybierz '5', aby zakończyć")

    try:
        num = int(input("Witaj, co chcesz zrobić: "))
        
        if 1 <= num <= 5:
            if num == 1:
                title = input("Czego ma dotyczyć? : ")
                definition = input("Podaj definicję: ") 
                definitions[title] = definition
                print("Definicja dodana pomyślnie.")
            elif num == 2:
                title = input("Wyszukaj po ID: ")
                if title in definitions:
                    print(definitions[title])
                else:
                    print("Nie ma takiej definicji.")
            elif num == 3:
                title = input("Podaj ID, które chcesz usunąć: ")
                if title in definitions:
                    del definitions[title]
                    print("Definicja usunięta pomyślnie.")
                else:
                    print("Nie ma takiej definicji.")
            elif num == 4:
                print(definitions)
            elif num == 5:
                print("Pa")
                break
        else:
            print("Podaj poprawny kod menu.")
    except ValueError:
        print("Błąd! Wprowadź poprawną wartość.")
