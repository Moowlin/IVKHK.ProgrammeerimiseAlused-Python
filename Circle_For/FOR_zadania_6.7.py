# ------------------------------------------------= ЗАДАЧА №1 =---------------------------------------------------------
# Создать программу, которая рисует изображение прямоугольника. Длины сторон прямоугольника указываются пользователем. 
# Прямоугольник можно нарисовать с помощью *. 2 варианта: использовать for и while.
# ----------------------------------------------------------------------------------------------------------------------
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
