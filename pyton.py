"""liczby = [1,2,3,4,5,6,7]

potegi = [ el ** 2
            for el in liczby]

parzyste = [ el
             for el in liczby
             if el % 2 == 0
             ]
print(parzyste)
print(potegi)


evenNumGenerations = (el ** 2
                        for el in range(101)
                        )
for i in evenNumGenerations:
    print(i)
"""
"""
names = {'arek', 'dawwadaw', 'adawdawdawdqwdaad', 'adw', 'daadwwwwwwwwwwwwwwwwa'}

namesLength = {
    name
    for name in names
    if not name.startswith('a')
}

print(namesLength)

numbers = [1,2,3,4,5,6,7,8]

multi = {
    num : num ** 3
    for num in numbers
}
print(multi)

celsius = {'tk' : 30, 'tl' : 15, 'ty' : 10, 'to' : 5, 't5' : 2}
fahrentheit = {
    key : (el*2)+ 30
    for key, el in celsius.items()
}

print(fahrentheit)
"""

wynik = [ el
          for el in range(471)
          if el % 7 == 0
          if not el % 5 == 0
          if el >= 100
]

print(wynik)
