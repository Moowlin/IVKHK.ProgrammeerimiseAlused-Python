'''
1. повторять пока пользователь не введет верно
• четное число
• нечетное число
• положительное число
• отрицательное число
'''
print('Задача 1')
print('МЕНЮ')
print('Выберите, когда остановим цикл:', 
        '1 - четное число', 
        '2 - нечетное число',
        '3 - положительное число',
        '4 - отрицательное число',
        '0 - завершиь программу', sep='\n')

n = -1
while n not in range(5):
    try:
        n = int(input('Ваш выбор: '))
    except ValueError:
        print('Это недопустимое значение')
    if n not in range(5):
        print('Такого пункта меню нет. Повторите ввод')

if n == 0: 
    print('До скорых встреч!')

if n == 1:
    print('Цикл не завершится пока не введете четное число')
    try:
        while int(input()) % 2 != 0:
            print('введите число')
        print('цикл завершен')
    except ValueError:
        print('Это недопустимое значение')

if n == 2:
    print('Цикл не завершится пока не введете нечетное число')
    print('введите число')
    try:
        while int(input()) % 2 == 0:
            print('введите число')
        print('цикл завершен')
    except ValueError:
        print('Это недопустимое значение')

if n == 3:
    print('Цикл не завершится пока не введете положительное число')
    print('введите число')
    try:
        while int(input()) < 0:
            print('введите число')
    except ValueError:
        print('Это недопустимое значение')
    print('цикл завершен')

if n == 4:
    print('Цикл не завершится пока не введете отрицательное число')
    print('введите число')
    try:
        while int(input()) > 0:
            print('введите число')
    except ValueError:
        print('Это недопустимое значение')
    print('цикл завершен')



'''
 2. пользователь вводит числа, найти сумму всех чисел, их количество и среднее значение.
Для окончания ввода ввести 0
'''



'''
3.	программa - БАНКОМАТ
•	Проверка кода пользователя (ввод 3 раза)
•	Сумма счета - случайное число
•	Операции: положить деньги, снять, посмотреть остаток счета, выйти из программы
•	Контроль, достаточно ли денег на счете для снятия денег
'''