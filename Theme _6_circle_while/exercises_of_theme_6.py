'''
1. ЗАДАЧА «СПИСОК КВАДРАТОВ»
По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N,
в порядке возрастания.
'''
print('Задача 1')
n = int(input('введите целое число '))
x = 1
while x**2 <= n:
    print(x ** 2)
    x = x + 1
print()

'''
2. ЗАДАЧА «МИНИМАЛЬНЫЙ ДЕЛИТЕЛЬ»
Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
'''
print('Задача 2')
n = int(input('введите целое число '))
x = 2
while x <= n:
    if n % x == 0:
        print(x)
        break
    x = x + 1
print()

'''
3. ЗАДАЧА «СТЕПЕНЬ ДВОЙКИ»
По данному натуральному числу N найдите наибольшую целую степень двойки, не
превосходящую N. Выведите показатель степени и саму степень.
Операцией возведения в степень пользоваться нельзя!
'''
print('Задача 3')
n = int(input('введите целое число '))
count = 0
x = 2
while x <= n:
    x *= 2
    count += 1
print(count, x // 2)
print()

'''
4. ЗАДАЧА «УТРЕННЯЯ ПРОБЕЖКА»
В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на
10% от предыдущего значения. По данному числу y определите номер дня, на который пробег
спортсмена составит не менее y километров.
Программа получает на вход действительные числа x и y и должна вывести одно натуральное
число.
'''
print('Задача 4')
x = int(input('В первый день спортсмен пробежал, км '))
y = int(input('Максимальное расстояние, км '))
days = 1
while x < y:
    x = x + x*0.1
    days = days + 1
print(days)
print()

'''
5. ЗАДАЧА «БАНКОВСКИЕ ПРОЦЕНТЫ»
Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов, после чего
дробная часть копеек отбрасывается. Определите, через сколько лет вклад составит не менее y рублей.
Выражение «дробная часть копеек отбрасывается» означает, что если у вас оказалось 123.4567
рублей, т. е. 123 рубля и 45.67 копеек, то после округления у вас получится 123 рубля и 45 копеек,
т.е. 123.45 рублей.
Программа получает на вход три натуральных числа: x, p, y и должна вывести одно целое число.
2
'''
print('Задача 5')
x = round(float(input('Вклад в банке составляет ')), 2)
p = int(input('Процент вклада равен '))
y = round(float(input('Максимальный размер вклада ')), 2)
years = 1
while x <= y:
    x = x + x/100*p



'''
6. ЗАДАЧА «ДЛИНА ПОСЛЕДОВАТЕЛЬНОСТИ»
Программа получает на вход последовательность целых неотрицательных чисел, каждое число
программно генерируется генератором случайных чисел и выводится на экран.
Если сгенерировано число 0, то программа должна закончить свою работу и вывести количество
сгенерированных чисел в последовательности (не считая завершающего числа 0).
'''
'''
7. ЗАДАЧА «СУММА ПОСЛЕДОВАТЕЛЬНОСТИ»
Программа получает на вход последовательность целых неотрицательных чисел, каждое число
программно генерируется генератором случайных чисел и выводится на экран.
Если сгенерировано число 0, то программа должна закончить свою работу и вывести сумму всех
элементов последовательности.
'''
'''
8. ЗАДАЧА «МАКСИМУМ И СРЕДНЕЕ ЗНАЧЕНИЕ
ПОСЛЕДОВАТЕЛЬНОСТИ»
Программа получает на вход последовательность целых неотрицательных чисел, каждое число
программно генерируется генератором случайных чисел и выводится на экран.
Если сгенерировано число 0, то программа должна закончить свою работу и вывести значение
наибольшего элемента последовательности и среднее значение последовательности .
'''
'''
9. ЗАДАЧА «ИНДЕКС МАКСИМУМА ПОСЛЕДОВАТЕЛЬ-
НОСТИ»
Программа получает на вход последовательность целых неотрицательных чисел, каждое число
программно генерируется генератором случайных чисел и выводится на экран.
Если сгенерировано число 0, то программа должна закончить свою работу и вывести индекс
наибольшего элемента последовательности. Если наибольших элементов несколько, выведите
индекс первого из них.
'''
'''
10. ЗАДАЧА « МАКСИМУМ ПОСЛЕДОВАТЕЛЬНОСТИ И
КОЛИЧЕСТВО ЕЁ ЭЛЕМЕНТОВ»
Программа получает на вход последовательность целых неотрицательных чисел, каждое число
программно генерируется генератором случайных чисел и выводится на экран.
Если сгенерировано число 0 или количество уже сгенерированных данных больше 20, то
программа должна закончить свою работу и вывести значение наибольшего элемента
последовательности и количество элементов
'''
