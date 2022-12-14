# https://informatics.msk.ru/

def create2dListNum(STR, STL, start, stop):
    from random import randint
    A = []
    for i in range(STR):
        A.append([randint(start, stop) for j in range(STL)])
    return A

def create2dListSymbol(STR, STL, symbol):
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


# -------------------------------------= 1. ЗАДАЧА «МАКСИМУМ» =---------------------------------------------------------
# Найдите индексы первого вхождения максимального элемента.
# Выведите два числа: номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве.
# Если таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны то тот, у
# которого меньше номер столбца.
# Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.
# ----------------------------------------------------------------------------------------------------------------------

print('1. ЗАДАЧА «МАКСИМУМ»')
n = int(input('Укажите количество строк: '))
m = int(input('Укажите количество столбцов: '))
matrix = create2dListNum(n, m, 1, 10)
print('Сгенерированная матрица:')
print2dArray(matrix)
max_num = matrix[0][0]
for i in range(n):
    for j in range(m):
        if matrix[i][j] > max_num:
            max_num = matrix[i][j]
            STR = i
            STL = j
print(f'Максимальный элемент: {max_num}')
print(f"Номер строки: {STR + 1}")
print(f"Номер столбца: {STL+1}")

# -------------------------------------= 2. ЗАДАЧА «СНЕЖИНКА» =---------------------------------------------------------
# Дано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив его символами "." (каждый элемент массива
# является строкой из одного символа).
# Затем заполните символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную диагональ.
# В результате символы "*" в массиве должны образовывать изображение снежинки.
# Выведите полученный массив на экран, разделяя элементы массива пробелами.
# ----------------------------------------------------------------------------------------------------------------------
print('2. ЗАДАЧА «СНЕЖИНКА»')
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

snowflakes = create2dListSymbol(n, n, '.')
for j in range(n):
    snowflakes[int(n/2+0.5)-1][j] = '*'
for i in range(n):
    snowflakes[i][int(n/2+0.5)-1] = '*'
for i in range(n):
    for j in range(n):
        if i == j:
            snowflakes[i][j] = '*'
            snowflakes[i][-j-1] = '*'
print2dArray(snowflakes)
print()

# -------------------------------------= 3. ЗАДАЧА «ШАХМАТНАЯ ДОСКА» =--------------------------------------------------
# Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке.
# В левом верхнем углу должна стоять точка.
# ----------------------------------------------------------------------------------------------------------------------
print('3. ЗАДАЧА «ШАХМАТНАЯ ДОСКА»')
n = int(input('Укажите количество строк: '))
m = int(input('Укажите количество столбцов: '))
result = []

for i in range(n):
    STR = []
    for j in range(m):
        if i % 2 == 0:
            if j % 2 == 0:
                STR.append('.')
            else:
                STR.append('*')
        else:
            if j % 2 == 0:
                STR.append('*')
            else:
                STR.append('.')
    result.append(STR)
print2dArray(result)
print()

# -------------------------------------= 4. ЗАДАЧА «ДИАГОНАЛИ, ПАРАЛЛЕЛЬНЫЕ ГЛАВНОЙ» =----------------------------------
# Дано число n. Создайте массив размером n×n и заполните его по следующему правилу. На главной диагонали должны быть
# записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.
# ----------------------------------------------------------------------------------------------------------------------
print('4. ЗАДАЧА «ДИАГОНАЛИ, ПАРАЛЛЕЛЬНЫЕ ГЛАВНОЙ»')
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

result = create2dListSymbol(n, n, '.')
for i in range(n):
    for j in range(n):
        result[i][j] = abs(i-j)
        # for u in range(n):
        #   if j == i+u or j == i-u:
        #      result[i][j] = u
print2dArray(result)
print()

# -------------------------------------= 5. ЗАДАЧА «ПОБОЧНАЯ ДИАГОНАЛЬ» =-----------------------------------------------
# Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
# Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
# Числа, стоящие выше этой диагонали, равны 0.
# Числа, стоящие ниже этой диагонали, равны 2.
# Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
# ----------------------------------------------------------------------------------------------------------------------
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

# -------------------------------------= 6. ЗАДАЧА «ПОМЕНЯТЬ СТОЛБЦЫ» =-------------------------------------------------
# Дан двумерный массив и два числа: i и j.
# Поменяйте в массиве столбцы с номерами i и j и выведите результат.
# Программа получает на вход размеры массива n и m, затем элементы массива,
# затем числа i и j.
# Решение оформите в виде функции swap_columns(a, i, j).
# ----------------------------------------------------------------------------------------------------------------------
print('6. ЗАДАЧА «ПОМЕНЯТЬ СТОЛБЦЫ»')

def swap_columns(a, st1, st2):
    n = len(a)
    m = len(a[0])
    for i in range(n):
        for j in range(m):
            x = a[i][st1-1]
            a[i][st1-1] = a[i][st2-1]
            a[i][st2 - 1] = x
    return a

n = int(input('Укажите количество строк: '))
m = int(input('Укажите количество столбцов: '))
a = create2dListNum(n, m, 1, 9)
print('Исходный массив')
print2dArray(a)

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

print('Новый массив массив')
a = swap_columns(a, i, j)
print2dArray(a)
print()
