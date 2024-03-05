table = [-5,-2,-1,0,1,2,3,4,5,6,7,8]
list = []

def sumAll(table):
    for i in table:
        if i > 0 :
           list.append(i)
           newList = sum(list)
    print(newList)

sumAll(table)



def sum_positives(numbers):
    return sum([number for number in numbers if number > 0])
 
numbers = [-5,-2,-1,0,1,2,3,4,5,6,7,8]
print(sum_positives(numbers)) 

