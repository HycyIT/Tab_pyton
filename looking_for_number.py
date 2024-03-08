import time


def times(func, *arg):
    sum = 0
    for i in range(0, 300):
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum = sum + (end - start)
    return sum


setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]


def numberSet(num, container):
    if num in container:
        return True
    else:
        return True


def numberList(num, container):
    if num in container:
        return True
    else:
        return False


print(times(numberSet, 30, setContainer))
print(times(numberList, 30, listContainer))
