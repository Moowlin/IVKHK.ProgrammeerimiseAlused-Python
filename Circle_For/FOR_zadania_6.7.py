# ------------------------------------------------= ЗАДАЧА №1 =---------------------------------------------------------
# Создать программу, которая рисует изображение прямоугольника. Длины сторон прямоугольника указываются пользователем. 
# Прямоугольник можно нарисовать с помощью *. 2 варианта: использовать for и while.
# ----------------------------------------------------------------------------------------------------------------------
'''
print('ЗАДАЧА №1')
print('Задайте стороны прямоугольника')
height, width = None, None
while True:
    try:
        height = int(input('Задайте высоту: '))
        if height <= 0:
            raise Exception
    except ValueError:
        print('Это недопустимое значение')
    except Exception:
            print("Высота не может быть меньше или равной 0")
    if (height is not None) and (height > 0):
        break

while True:
    try:
        width = int(input('Задайте ширину: '))
        if width <= 0:
            raise Exception
    except ValueError:
        print('Это недопустимое значение')
    except Exception:
            print("Ширина не может быть меньше или равной 0")
    if (width is not None) and (width > 0):
        break

for i in range(height):
    for j in range(width):
        print('* ', end='')
    print()
'''
# ------------------------------------------------= ЗАДАЧА №2 =---------------------------------------------------------
# Создать программу деления для чисел от 1 до n (вводит пользователь). В каждом ряду должны распечатать число и столько 
# плюсов, сколько делителей у этого числа: 
# ----------------------------------------------------------------------------------------------------------------------
'''
print('ЗАДАЧА №2')
N = None
while True:
    try:
        N = int(input('Задайте число: '))
    except ValueError:
        print('Это недопустимое значение')
    if N is not None:
        break
for j in range(1, N + 1):
    print(j,': ', end='')
    for d in range(1, j+1):
        if j % d == 0:
            print("+ ", end='')
    print()
'''
# ------------------------------------------------= ЗАДАЧА №3 =---------------------------------------------------------
# Создать программу деления для чисел от 1 до 25. В каждом ряду должны распечатать число и делители у этого числа: 
# ----------------------------------------------------------------------------------------------------------------------
'''
print('ЗАДАЧА №3')
for j in range(1, 26):
    print(j,': ', end='')
    for d in range(1, j+1):
        if j % d == 0:
            print(d, end=' ')
    print()
'''
# ------------------------------------------------= ЗАДАЧА №4 =---------------------------------------------------------
# Рисование треугольников. Пользователь задает кол-во строк
# ----------------------------------------------------------------------------------------------------------------------
print('ЗАДАЧА №4')
N = None
while True:
    try:
        N = int(input('Задайте число: '))
        if N <= 0:
            raise Exception
    except ValueError:
        print('Это недопустимое значение')
    except Exception:
        print('Это недопустимое значение')
    if N is not None and N > 0:
        break

for i in range(1, N+1):
    print('*' * i)
print()

for i in range(N, 0, -1):
    print(' ' * (N-i), "*"*i, sep='')
print()

for i in range(N, 0, -1):
    print('*' * i)
print()

for i in range(1, N+1):
    print(' ' * (N-i), "*"*i, sep='')
print()
