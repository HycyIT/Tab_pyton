import time


def sumuj_do(num):
    suma = 0
    for i in range(1, num + 1):
        suma += i
    return suma


def sumuj_do2(num):
    return sum([num for num in range(1, num + 1)])


def sumuj_do3(num):
    return sum({num for num in range(1, num + 1)})


def sumuj_do4(num):
    return sum((num for num in range(1, num + 1)))


def finish_timer(start):
    end = time.perf_counter()
    return end - start


def function_performance(func, arg, how_many=1):
    sum = 0
    for i in range(0, how_many):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end - start)
    return sum


def show_message(message):
    print(message)


print(function_performance(sumuj_do, 50000, 20))
print(function_performance(sumuj_do2, 50000))
print(function_performance(sumuj_do3, 50000))
print(function_performance(sumuj_do4, 50000))
