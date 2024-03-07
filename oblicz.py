import figury
from enum import IntEnum

Menu_Figury = IntEnum('Menu_Figury', 'Kwadrat Prostokąt Trójkąt Trapez Koło')
wybor = int(input("""Wybierz figure którą chcesz policzyć
1.Kwadrat
2.Prostokąt
3.Trójkąt
4.Trapez
5.Koło

Twój wybór : """))

if (wybor == Menu_Figury.Kwadrat):
    a = float(input("Podaj a : "))
    print(figury.pole_kwadratu(a))        
elif wybor == Menu_Figury.Prostokąt:
    a = float(input("Podaj 'a': "))
    b = float(input("Podaj 'b': ")) 
    print(figury.pole_prostokata(a, b))
elif wybor == Menu_Figury.Trójkąt:
    a = float(input("Podaj 'a': "))
    h = float(input("Podaj 'h': "))
    print(figury.pole_trojkata(a, h))
elif wybor == Menu_Figury.Trapez:
    a = float(input("Podaj 'a': "))
    b = float(input("Podaj 'b': "))
    h = float(input("Podaj 'h': "))
    print(figury.pole_trapezu(a, b, h))
elif wybor == Menu_Figury.Koło:
    r = float(input("Podaj 'r': "))
    print(figury.pole_kola(r))
