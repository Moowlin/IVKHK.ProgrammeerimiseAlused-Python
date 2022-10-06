'''
• Знаки гороскопа
Создайте блок-схему и реализуйте программу
Пользователь вводит два целых числа: D (день) и M (месяц), которые определяют правильную дату. 
Покажите знак зодиака, соответствующий дате: 
«Водолей» (20.1-18.2), «Рыбы» (19.2-20.3), «Овен» (21.3-19.4), 
«Телец» (20.4-20.5), «Близнецы» ( 21.5-21.6), «Рак» (22.6-22.7), 
«Лев» (23.7-22.8), «Дева» (23.8-22.9), «Весы» (23.9-22.10), 
«Скорпион» (23.10-22.11), «Стрелец» (23.11-21.12), «Козерог» (22.12-19.1).
'''

def CheckingDate(M, D):
    if M in (1, 3, 5, 7, 8, 10, 12) and D in range(1, 32):
        return 'OK'
    elif M == 2 and D in range(1, 30):
        return 'OK'
    elif M in (4, 6, 9, 11) and D in range(1, 31):
        return 'OK'
    else:
        return 'NOT'

D, M = 0, 0
while D not in range(1, 32) and M not in range(1, 13):
    D = int(input('Введите номер дня '))
    M = int(input('Введите номер месяца '))
    if D not in range(1, 32) or M not in range(1, 13):
        print('Вы ввели неверные значения. Повторите ввод.')
    elif CheckingDate(M, D) == 'NOT':
        print('Введите существующую дату')

if (M == 1 and 20 <= D <= 31) or (M == 2 and 1 <= D <= 18):
    print('Водолей')
elif (M == 2 and 19 <= D <= 29) or (M == 3 and 1 <= D <= 20):
    print('Рыбы')
elif (M == 3 and 21 <= D <= 31) or (M == 4 and 1 <= D <= 19):
    print('Овен')
elif (M == 4 and 20 <= D <= 30) or (M == 5 and 1 <= D <= 20):
    print('Телец')
elif (M == 5 and 21 <= D <= 31) or (M == 6 and 1 <= D <= 21):
    print('Близнецы')
elif (M == 6 and 22 <= D <= 30) or (M == 7 and 1 <= D <= 22):
    print('Рак')
elif (M == 7 and 23 <= D <= 31) or (M == 8 and 1 <= D <= 22):
    print('Лев')
elif (M == 8 and 23 <= D <= 31) or (M == 9 and 1 <= D <= 22):
    print('Дева')
elif (M == 9 and 23 <= D <= 30) or (M == 10 and 1 <= D <= 22):
    print('Весы')
elif (M == 10 and 23 <= D <= 31) or (M == 11 and 1 <= D <= 22):
    print('Скорпион')
elif (M == 11 and 23 <= D <= 30) or (M == 12 and 1 <= D <= 21):
    print('Стрелец')
elif (M == 12 and 21 <= D <= 31) or (M == 1 and 1 <= D <= 19):
    print('Козерог')
