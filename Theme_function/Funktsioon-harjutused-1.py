# -----------------------------------------------------= Задача 1 =-----------------------------------------------------
# 1. Täiusta defineeritud ruudu joonistamise funktsiooni nii, et ruudu küljepikkuse saab määrata funktsiooni
# väljakutsel. Kasuta loodud funktsiooni, joonistades mitu erineva suurusega ruutu.

# 1. Улучшить функцию рисования заданного квадрата, чтобы длину стороны квадрата можно было определить в вызове функции.
# Используйте созданную функцию, нарисовав несколько квадратов разного размера.
# ----------------------------------------------------------------------------------------------------------------------

def square():
    a = int(input('Укажите сторону квадрата: '))
    print('* ' * a)
    for i in range(a-2):
        print('* ' + '  '*(a-2)+ "*")
    print('* ' * a)

square()
















