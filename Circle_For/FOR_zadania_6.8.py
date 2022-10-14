# ----------------------------------------= 1. ЗАДАЧА «РЯД - 1» =-------------------------------------------------------
# Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.
# ----------------------------------------------------------------------------------------------------------------------
print('ЗАДАЧА №1')
print('Задайте числа А и В, при этом A ≤ B:')
A, B = None, None
while True:
    try:
        A = int(input('введите число A: '))
    except ValueError:
        print('Это недопустимое значение')
    if A is not None:
        while True:
            try:
                B = int(input('введите число B: '))
                if A > B:
                    raise Exception
            except ValueError:
               print('Это недопустимое значение')
            except Exception:
                print("Число B не должно быть меньше A")
            if B is not None:
                break
    if A is not None and B is not None and A <= B:
        break
for i in range(A, B + 1):
    print(i, end=' ')
print()

# ----------------------------------------= 2. ЗАДАЧА «РЯД - 2» =-------------------------------------------------------
# Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в
# порядке убывания в противном случае.
# ----------------------------------------------------------------------------------------------------------------------
print('ЗАДАЧА №2')
print('Задайте числа А и В, числа должны быть различными')
A, B = None, None
while True:
    try:
        A = int(input('введите число A: '))
    except ValueError:
        print('Это недопустимое значение')
    if A is not None:
        while True:
            try:
                B = int(input('введите число B: '))
                if A == B:
                    raise Exception
            except ValueError:
               print('Это недопустимое значение')
            except Exception:
                print("Число B не должно быть равно A")
            if B is not None:
                break
    if A is not None and B is not None and A != B:
        break
if A < B:
    for i in range(A, B + 1):
        print(i, end=' ')
if A > B:
    for i in range(A, B - 1, -1):
        print(i, end=' ')
print()

# ----------------------------------------= 3. ЗАДАЧА «РЯД - 3» =-------------------------------------------------------
# Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно. В этой задаче нельзя использовать
# инструкцию if в теле цикла.
# ----------------------------------------------------------------------------------------------------------------------
print('ЗАДАЧА №3')
print('Задайте числа А и В, при этом A > B:')
A, B = None, None
while True:
    try:
        A = int(input('введите число A: '))
    except ValueError:
        print('Это недопустимое значение')
    if A is not None:
        while True:
            try:
                B = int(input('введите число B: '))
                if A < B:
                    raise Exception
            except ValueError:
                print('Это недопустимое значение')
            except Exception:
                print("Число B должно быть меньше A")
            if B is not None:
                break
    if A is not None and B is not None and A > B:
        break
if A % 2 == 0:
    A -= 1
for i in range(A, B - 1, -2):
    print(i, end=' ')
print()

# ----------------------------------------= 4. ЗАДАЧА «СУММА ДЕСЯТИ ЧИСЕЛ» =--------------------------------------------
# Дано 10 целых чисел. Числа сгенерированы случайным образом. Вычислите их сумму.
# ----------------------------------------------------------------------------------------------------------------------
print('ЗАДАЧА №4')
from random import randint
N, V = None, None
while True:
    try:
        N = int(input('Укажите нижнюю границу диапазона генерации чисел: '))
    except ValueError:
        print('Это недопустимое значение')
    if N is not None:
        while True:
            try:
                V = int(input('Укажите верхнюю границу диапазона генерации чисел: '))
                if V < N:
                    raise Exception
            except ValueError:
                print('Это недопустимое значение')
            except Exception:
                print("Верхняя граница должна быть больше")
            if V is not None:
                break
    if N is not None and V is not None and V > N:
        break
result = 0
numbers = []
for i in range(10):
    x = randint(N, V)
    numbers.append(x)
    result += x
print(f'Диапазон генерации чисел ({N}:{V})')
print(f'Сгенерированы числа: ', *numbers)
print(f'Сумма чисел равна {result}')
print()

# ----------------------------------------= 5. ЗАДАЧА «СУММА N ЧИСЕЛ» =-------------------------------------------------
# Сначала вводите количество чисел N, затем выводится на экран ровно N целых чисел сгенерированных случайным образом.
# Вычислите их сумму.
# ----------------------------------------------------------------------------------------------------------------------

print('ЗАДАЧА №5')
from random import randint
N, V, K = None, None, None
while True:
    try:
        N = int(input('Укажите нижнюю границу диапазона генерации чисел: '))
    except ValueError:
        print('Это недопустимое значение')
    if N is not None:
        while True:
            try:
                V = int(input('Укажите верхнюю границу диапазона генерации чисел: '))
                if V <= N:
                    raise Exception
            except ValueError:
                print('Это недопустимое значение')
            except Exception:
                print("Верхняя граница должна быть больше")
            if V is not None:
                break
    if N is not None and V is not None and V > N:
        break
while True:
    try:
        K = int(input('Укажите количество генерируемых чисел: '))
        if K <= 0:
            raise Exception
    except ValueError:
        print('Это недопустимое значение')
    except Exception:
        print("Количество должно быть больше нуля")
    if K is not None and K > 0:
        break
result = 0
numbers = []
for i in range(K):
    x = randint(N, V)
    numbers.append(x)
    result += x
print(f'Диапазон генерации чисел ({N}:{V})')
print(f'Сгенерированы числа: ', *numbers)
print(f'Сумма чисел равна {result}')
print()

# ----------------------------------------= 6. ЗАДАЧА «СУММА КУБОВ» =---------------------------------------------------
# По данному натуральном n вычислите сумму 1^3+2^3+3^3+...+n^3.
# ----------------------------------------------------------------------------------------------------------------------

print('ЗАДАЧА №6')
N = None
while True:
    try:
        N = int(input('Укажите число от 1 до 99999: '))
        if N not in range(1, 100000):
            raise Exception
    except ValueError:
        print('Это недопустимое значение')
    except Exception:
        print("Количество должно быть в диапазоне от 1 до 99999 ")
    if N is not None and N in range(1, 100000):
        break
result = 0
for i in range(1, N+1):
    result += i ** 3
print(f'сумма кубов сгенерированных чисел равна {result}')

# ----------------------------------------= 7. ЗАДАЧА «ФАКТОРИАЛ» =-----------------------------------------------------
# Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!. По данному натуральному n вычислите
# значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.
# ----------------------------------------------------------------------------------------------------------------------
print('ЗАДАЧА №7')
N = None
while True:
    try:
        N = int(input('Укажите число от 1 до 999: '))
        if N not in range(1, 1000):
            raise Exception
    except ValueError:
        print('Это недопустимое значение')
    except Exception:
        print("Количество должно быть в диапазоне от 1 до 999 ")
    if N is not None and N in range(1, 1000):
        break
result = 1
for i in range(1, N+1):
    result *= i
print(f'Факториал равен {result}')
print()

# ----------------------------------------= 8. ЗАДАЧА «СУММА ФАКТОРИАЛОВ» =---------------------------------------------
# По данному натуральному числу n вычислите сумму 1!+2!+3!+...+n!. В решении этой задачи желательно использовать только
# один цикл. Пользоваться математической библиотекой math в этой задаче запрещено.
# ----------------------------------------------------------------------------------------------------------------------
print('ЗАДАЧА №8')
N = None
while True:
    try:
        N = int(input('Укажите число от 1 до 999: '))
        if N not in range(1, 1000):
            raise Exception
    except ValueError:
        print('Это недопустимое значение')
    except Exception:
        print("Количество должно быть в диапазоне от 1 до 999 ")
    if N is not None and N in range(1, 1000):
        break
result = 0
y = 1
for i in range(1, N+1):
    y = y * i
    result += y
print(f'Сумма факториалов равна  {result}')
print()

# ----------------------------------------= 9. ЗАДАЧА «КОЛИЧЕСТВО НУЛЕЙ» =----------------------------------------------
# Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел. Для ввода данных предложите цикл – выход
# из цикла ввод пустой строки (нажатие ENTER). Подсчитайте количество нулей среди введенных чисел и выведите это
# количество.
# ----------------------------------------------------------------------------------------------------------------------
print('ЗАДАЧА №9')
'''
from random import randint
N, V, K = None, None, None
while True:
    try:
        N = int(input('Укажите нижнюю границу диапазона генерации чисел: '))
    except ValueError:
        print('Это недопустимое значение')
    if N is not None:
        while True:
            try:
                V = int(input('Укажите верхнюю границу диапазона генерации чисел: '))
                if V <= N:
                    raise Exception
            except ValueError:
                print('Это недопустимое значение')
            except Exception:
                print("Верхняя граница должна быть больше")
            if V is not None:
                break
    if N is not None and V is not None and V > N:
        break
while True:
    try:
        K = int(input('Укажите количество генерируемых чисел: '))
        if K <= 0:
            raise Exception
    except ValueError:
        print('Это недопустимое значение')
    except Exception:
        print("Количество должно быть больше нуля")
    if K is not None and K > 0:
        break
count = 0
numbers = []
for i in range(K):
    x = randint(N, V)
    numbers.append(x)
    if x == 0:
        count += 1
print(f'Диапазон генерации чисел ({N}:{V})')
print(f'Сгенерированы числа: ', *numbers)
print(f'Количество нулей в последовательности {count}')
print()
'''

N = None
while True:
    try:
        N = int(input('Укажите целое положительное число больше 0 '))
        if N <= 0:
            raise Exception
    except ValueError:
        print('Это недопустимое значение')
    except Exception:
        print('Это недопустимое значение')
    if N is not None and N > 0:
        break

print(f'Вводите целые числа, у вас не более {N} попыток, для завершения цикла раньше введите пустую строку')
Flag = True
count = 0
for i in range(1, N + 1): 
    while Flag == True:
        try:
            num = input(f'У вас осталось {N-i} попыток. Введите число ')
            if num == '':
                print('до свидания!')
                Flag = False
                break
            if num.isdigit() == False:
                num = None
                raise Exception
        except Exception:
            print('Это недопустимое значение')
        if num is not None:
            print(num)
            break
    if Flag == False:
        break
    for j in num:
        if j == "0":
            count += 1
print(f'введено {count} нулей')
print()

# ----------------------------------------= 10. ЗАДАЧА «ЛЕСЕНКА» =------------------------------------------------------
# По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов
# (вложенные циклы).
# ----------------------------------------------------------------------------------------------------------------------
print('ЗАДАЧА №10')
N = None
while True:
    try:
        N = int(input('Укажите число от 1 до 9: '))
        if N not in range(1, 10):
            raise Exception
    except ValueError:
        print('Это недопустимое значение')
    except Exception:
        print("Число должно быть в диапазоне от 1 до 9")
    if N is not None and N in range(1, 10):
        break
for i in range(1, N+1):
    print()
    for j in range(1, i+1):
        print(j, end=" ")
print()
print()

# ----------------------------------------= 11. ЗАДАЧА «ПОТЕРЯННАЯ КАРТОЧКА» =------------------------------------------
# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. Найдите ее, зная номера
# оставшихся карточек. Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N). Программа должна
# вывести номер потерянной карточки (вложенные циклы).
# массивами и аналогичными структурами данных пользоваться нельзя.
# ----------------------------------------------------------------------------------------------------------------------
print('ЗАДАЧА №11')
N = None
while True:
    try:
        N = int(input('Укажите количество карточек в игре: '))
        if N <= 0:
            raise Exception('Это недопустимое значение')
    except ValueError:
        print('Это недопустимое значение')
    except Exception as e:
        print(e)
    if N is not None and N > 0:
        break

summa_etalon = 0
for i in range(1, N+1):
    summa_etalon += i

koloda = []     # используется ТОЛЬКО для проверки введенных номеров карточек
summa_user = 0
print(f'Вы должны указать номера {N-1} карт')
for i in range(1, N):
    while True:
        try:
            verification = True
            karta = int(input(f'Укажите номер {i}-й карты: '))
            if karta in koloda:
                verification = False
                raise Exception('Этот номер уже был. Укажите другой номер')
            if karta not in range(1, N+1):
                verification = False
                raise Exception('Данной карты нет в колоде. Укажите другой номер')
        except ValueError:
            verification = False
            print('Это недопустимое значение')
        except Exception as e:
            print(e)
        if verification == True:
            break
    koloda.append(karta)
    summa_user += karta
lost_karta = summa_etalon - summa_user
print(f'Номер потерянной карты: {lost_karta}')
