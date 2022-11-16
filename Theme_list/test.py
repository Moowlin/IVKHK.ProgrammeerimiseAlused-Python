def create2dListNum(STR, STL, start, stop):
    from random import randint
    A = []
    for i in range(STR):
        A.append([randint(start, stop) for j in range(STL)])
    return A

def create2dListSymbol(STR, STL, symbol):
    from random import randint
    A = []
    for i in range(STR):
        A.append([symbol for j in range(STL)])
    return A

def createList(l, start, stop):
    from random import randint
    A = []
    for i in range(l):
        A.append(randint(start, stop))
    return A

def print2dArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()



print('5. ЗАДАЧА «ПОБОЧНАЯ ДИАГОНАЛЬ»')

while True:
    try:
        n = int(input('Укажите НЕЧЕТНОЕ число: '))
        if n % 2 == 0:
            raise Exception
    except ValueError:
        print('Введены некорректные данные')
    except Exception:
        print('Вы ввели четное число')
    else:
        print()
        break

result = create2dListSymbol(n, n, 0)

for i in range(n):
    for j in range(n):
        if i == j:
            result[i][-j - 1] = 1
        if i == j-1:
            result[i][-j - 1] = 0
        if j > len(result)-i-1:
            result[i][j] = 2
print2dArray(result)
print()