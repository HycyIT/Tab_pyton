definitions = {}

while True :
    print('     Wybierz 1 - aby dodać definicje')
    print('     Wybierz 2 - aby wyszukac definicje')
    print('     Wybierz 3 - aby usunąc definicje')
    print('     Wybierz 4 - aby wyświetlić cały słownik')
    print('     Wybierz 5 - aby zakończyć')
    
    try:
        num = int(input('   Wybierz co chcesz zrobic? : '))
        if 1 <= num <= 5:
            if num == 1 :
                title = input('Podaj tytuł definicji : ')
                definition = input('Podaj definicje : ')
                definitions[title] = definition
                print('Dodałeś definicje')
            if num == 2 :
                title = input('Podaj szukaną definicje : ')
                if title in definitions:
                     print(f'Definicja dla {title} to : {definitions[title]}')
                else :
                    print('Nie ma takiej definicji')
            if num == 3 :
                title = input('Podaj definicję do usunięcia')
                if title in definitions:
                    del(definitions[title])
                    print(f'Definicja {title} została usunięta')
                else :
                    print('Nie ma takiej definicji')
            if num == 4 :
                print(definitions)
            if num == 5 :
                print('Do zobaczenia')
                break
        else :
            print('Podaj liczbe z zakresu menu')
    except ValueError:
        print('Musisz podac liczbę')
