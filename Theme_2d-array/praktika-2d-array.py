# ------------------------------= Тема 10. Практика. ЗАДАНИЯ Двумерные массивы =----------------------------------------
# 1. создайте двумерный массив
# 2. заполните случайными числами
# 3. найдите сумму чисел по каждой строке, добавьте результаты в массив
# 4. найдите сумму чисел по каждой колонке, добавьте результаты в массив
# 5. поменяйте строки
# 6. поменяйте колонки
# 7. предложите функции для 5 и 6 задания
# ----------------------------------------------------------------------------------------------------------------------

def create2dListNum(STR, STL, start, stop):
    '''Функция создания матрицы размером STRxSTL, заполнение случайными числами из диапазона [start; stop]'''
    from random import randint
    A = []
    for i in range(STR):
        A.append([randint(start, stop) for j in range(STL)])
    return A

def print2dArray(arr):
    '''Функция печати массива'''
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()

def swap_columns(a, st1, st2):
    '''Функция перестановки столбцов местами'''
    n = len(a)
    m = len(a[0])
    for i in range(n):
        for j in range(m):
            x = a[i][st1-1]
            a[i][st1-1] = a[i][st2-1]
            a[i][st2 - 1] = x
    return a


def swap_lines(a, str1, str2):
    '''Функция перестановки столбцов местами'''
    n = len(a)
    m = len(a[0])
    for i in range(n):
        x = a[str1-1]
        a[str1-1] = a[str2-1]
        a[str2 - 1] = x
    return a


def copy2dArray(a):
    '''Функция копирования двумерного массива'''
    n = len(a)
    mx = []
    for i in a:
        mx.append(i.copy())
    return mx


# ---------------= MAIN =--------------------

n = int(input('Укажите количество строк: '))
m = int(input('Укажите количество столбцов: '))
OriginMatrix = create2dListNum(n, m, 1, 2)

matrix = copy2dArray(OriginMatrix)

print('Исходный массив: ')
print2dArray(matrix)

newStr = [0 for i in range(m)]

for i in range(n):
    summaSTR = 0
    for j in range(m):
        newStr[j] = newStr[j]+matrix[i][j]
        summaSTR += matrix[i][j]
    matrix[i].append(summaSTR)

matrix.append(newStr)
print('Суммы по строкам и столбцам: ')
print2dArray(matrix)
print()
print('Меняем столбцы местами:')
while True:
    try:
        i = int(input('Укажите номер столбца i: '))
        j = int(input('Укажите номер столбца j: '))
        if (i <= 0) or (i > m) or (j <= 0) or (j > m) or (i == j):
            raise Exception
    except ValueError:
        print('Введены некорректные данные')
    except Exception:
        print('Вы ввели некорректный номер столбца')
    else:
        print()
        break

a = copy2dArray(OriginMatrix)

print('Новый массив массив: ')
a = swap_columns(a, i, j)
print2dArray(a)

print()

b = copy2dArray(OriginMatrix)
print('Меняем строки местами:')
while True:
    try:
        i = int(input('Укажите номер строки i: '))
        j = int(input('Укажите номер строки j: '))
        if (i <= 0) or (i > n) or (j <= 0) or (j > n) or (i == j):
            raise Exception
    except ValueError:
        print('Введены некорректные данные')
    except Exception:
        print('Вы ввели некорректный номер столбца')
    else:
        print()
        break
print('Новый массив массив: ')
b = swap_lines(a, i, j)
print2dArray(b)







