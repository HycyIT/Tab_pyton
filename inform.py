import week

from enum import IntEnum

Menu_Week = IntEnum('Menu_Week', 'Poniedziałek Wtorek Środa Czwartek Piątek Sobota Niedziela')

choose = int(input("""Wybierz numer tygodnia :

1:Poniedziałek
2:Wtorek
3:Środa
4:Czwartek
5:Piątek
6:Sobota
7:Niedziela

Twój wybór to : """))

if (choose == Menu_Week.Poniedziałek):
    week.day_1()
elif (choose == Menu_Week.Wtorek):
    week.day_2()
elif (choose == Menu_Week.Środa):
    week.day_3()
elif (choose == Menu_Week.Czwartek):
    week.day_4()
elif (choose == Menu_Week.Piątek):
    week.day_5()
elif (choose == Menu_Week.Sobota):
    week.day_6()
elif (choose == Menu_Week.Niedziela):
    week.day_7()
    

    
