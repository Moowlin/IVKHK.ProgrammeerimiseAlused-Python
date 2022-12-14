#-------------------------------= ЗАДАЧА 1 =------------------------------#
# 1. повторять пока пользователь не введет верно
#  • четное число
# • нечетное число
# • положительное число
# • отрицательное число
#-------------------------------------------------------------------------#

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
    while True:
        try:
            x = int(input('введите число: '))
            if x  % 2 == 0:
                break
        except ValueError:
            print('Это недопустимое значение')


if n == 2:
    print('Цикл не завершится пока не введете нечетное число')
    while True:
        try:
            x = int(input('введите число: '))
            if x  % 2 != 0:
                break
        except ValueError:
            print('Это недопустимое значение')

if n == 3:
    print('Цикл не завершится пока не введете положительное число')
    while True:
        try:
            x = int(input('введите число: '))
            if x > 0:
                break
        except ValueError:
            print('Это недопустимое значение')

if n == 4:
    print('Цикл не завершится пока не введете отрицательное число')
    while True:
        try:
            x = int(input('введите число: '))
            if x < 0:
                break
        except ValueError:
            print('Это недопустимое значение')

print()


#-------------------------------= ЗАДАЧА 2 =------------------------------#
# 2. пользователь вводит числа, найти сумму всех чисел, их количество и среднее значение.
# Для окончания ввода ввести 0
#-------------------------------------------------------------------------#

print('Задача 2')
summa = 0
count = 0
while True:
    try:
        x = int(input('Для окончания ввода ввести 0. введите число: '))
        count += 1
        summa += x
        if x == 0:
            break
    except ValueError:
        print('Это недопустимое значение')
print(f'Сумма равна {summa}', 
        f'Количество равна {count}', 
        f'Среднее значение равно {round(summa / count, 2)}', sep='\n')

print()


#-------------------------------= ЗАДАЧА 3 =------------------------------#
# 3.	программa - БАНКОМАТ
# •	Проверка кода пользователя (ввод 3 раза)
# •	Сумма счета - случайное число
# •	Операции: положить деньги, снять, посмотреть остаток счета, выйти из программы
#-------------------------------------------------------------------------#
from random import randint
print('Задача 3')
print('Для начала работы задайте пароль. Для заверешения программы введите 0')
password_etalon = str()
password_user = str()
stop = False
#------------------= Задание пароля =------------------#
while len(password_etalon) < 8 or password_etalon != password_user:
    password_etalon = input('введите пароль, не менее 8 символов: ')
    if password_etalon == '0':
        print('До свидания')
        stop = True
        break
    elif len(password_etalon) < 8:
        print('недопустимый пароль')
    else:
        password_user = input('повторите пароль: ')
        if password_user == '0':
            print('До свидания')
            stop = True
            break
        if password_etalon != password_user:
            print('пароли не совпадают')
if stop == False:
    print('Пароль задан. Счет создан. Не забудьте его!')
account = randint(0, 1000)
#------------------= Банкомат =------------------#
while stop == False:
    print()
    print('Добро пожаловать в "Банкомат"! Для заверешения программы введите 0')
    print()
    #------------------= Проверка пароля =------------------#
    password_user = str()
    count = 3
    while password_etalon != password_user:
        print(f'Для входа в систему введите пароль. У Вас осталось {count} попыток')
        password_user = input()
        if password_user == '0':
            print('До свидания')
            stop = True
            break
        if password_user != password_etalon:
            count -= 1
        if count == 0:
            print('Вы ввели пароль неправильно три раза. До свидания!')
            stop = True
            break
    #------------------= Меню банкомата =------------------#
    print('МЕНЮ')
    print('1 - Посмотреть остаток счета', 
          '2 - Положить деньги на счет',
          '3 - Снять деньги',
          '0 - завершиь программу', sep='\n')
    user = 100
    while user not in range(4):
        try:
            user = int(input('укажите пункт меню '))
            if user == 0:
                stop = True
                print('До свидания')
                break
        except ValueError:
            print('Это недопустимое значение')

    if user == 1:
        print(f'Остаток счета равен {account}')
    
    if user == 2:
        summa = float(input('Укажите сумму: '))
        account = round(account + summa, 2)
        print(f'Остаток счета равен {account}')
    
    if user == 3:
        summa = float(input('Укажите сумму снятия: '))
        if summa > account:
            print('У вас недостаточно средств')
        else:
            account = account - summa
            print(f'Остаток счета равен {account}')