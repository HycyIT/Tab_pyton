def sumuj_do(num):
    suma = 0
    for i in range(1, num + 1):
        suma += i
    return suma


def sumuj_do2(num):
    return sum([num for num in range(1, num + 1)])


num = int(input("Podaj liczbe"))
print(sumuj_do(num))
print(sumuj_do2(num))