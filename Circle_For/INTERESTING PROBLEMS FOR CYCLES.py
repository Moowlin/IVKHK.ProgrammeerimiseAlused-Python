# -----------------------------------------------= ЗАДАЧА 1 =-----------------------------------------------------------
# Создайте программу, выводящую на экран все четырёхзначные числа последовательности 1000 1003 1006 1009 1012 1015 ....
# ----------------------------------------------------------------------------------------------------------------------
'''
print('ЗАДАЧА 1')
for i in range(1000, 10000, 3):
    print(i, end=' ')
print()
'''
# -----------------------------------------------= ЗАДАЧА 2 =-----------------------------------------------------------
# Создайте программу, выводящую на экран первые 55 элементов последовательности 1 3 5 7 9 11 13 15 17 ....
# ----------------------------------------------------------------------------------------------------------------------
'''
print('ЗАДАЧА 2')
count = 1
for i in range(1, 110, 2):
    count += 1
    if count == 55:
        break
    print(i, end=' ')
print()
'''
# -----------------------------------------------= ЗАДАЧА 3 =-----------------------------------------------------------
# Создайте программу, выводящую на экран все неотрицательные элементы последовательности 90 85 80 75 70 65 60 ....
# ----------------------------------------------------------------------------------------------------------------------
'''
print('ЗАДАЧА 3')
for i in range(90, -1, -5):
    print(i, end=' ')
print()
'''
# -----------------------------------------------= ЗАДАЧА 4 =-----------------------------------------------------------
# Создайте программу, выводящую на экран первые 20 элементов последовательности 2 4 8 16 32 64 128 ....
# ----------------------------------------------------------------------------------------------------------------------
'''
print('ЗАДАЧА 4')
for i in range(1, 21):
    print(2**i, end=' ')
print()
'''
# -----------------------------------------------= ЗАДАЧА 5 =-----------------------------------------------------------
# Выведите на экран все члены последовательности 2an-1–1, где a1=2, которые меньше 10000.
# ----------------------------------------------------------------------------------------------------------------------
'''
print('ЗАДАЧА 5')
print("Первый вариант решения:")
lst = [0, 2]
for n in range(2, 100):
    Anov = 2 * lst[n-1] - 1
    if Anov <= 10000:
        lst.append(Anov)
        print(lst[n], end=' ')
    else:
        break
print()

print("Второй вариант решения:")
A = 2
for n in range(2, 100):
    Anov = 2 * A - 1
    if Anov >= 10000:
        break
    else:
        print(Anov, end=' ')
        A = Anov
print()

print("Третий вариант решения (на мой взгляд самый удачный):")
A = 2
Anov = 0
while Anov < 10000:
    Anov = 2 * A - 1
    if Anov <= 10000:
        print(Anov, end=' ')
    A = Anov
'''
# -----------------------------------------------= ЗАДАЧА 6 =-----------------------------------------------------------
# Выведите на экран все двузначные члены последовательности 2an-1+200, где a1= –166.
# ----------------------------------------------------------------------------------------------------------------------
'''
print('ЗАДАЧА 6')
print("Первый вариант решения:")
A = -166
for n in range(2, 100):
    Anov = 2 * A + 200
    if Anov > -100 and Anov < 100:
        print(Anov, end=' ')
    if Anov > 100:
        break
    A = Anov
print()

print("Второй вариант решения (на мой взгляд более удачный):")
A = -166
Anov = 0
while Anov < 100:
    Anov = 2 * A + 200
    if Anov > -100 and Anov < 100:
        print(Anov, end=' ')
    A = Anov
print()
'''
# -----------------------------------------------= ЗАДАЧА 7 =-----------------------------------------------------------
# Создайте программу, вычисляющую факториал натурального числа n, которое пользователь введёт с клавиатуры.
# ----------------------------------------------------------------------------------------------------------------------
'''
print('ЗАДАЧА 7')
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
'''
# -----------------------------------------------= ЗАДАЧА 8 =-----------------------------------------------------------
# Выведите на экран все положительные делители натурального числа, введённого пользователем с клавиатуры.
# ----------------------------------------------------------------------------------------------------------------------
print('ЗАДАЧА 8')
N = None
while True:
    try:
        N = int(input('Укажите число: '))
    except ValueError:
        print('Это недопустимое значение')
    if N is not None:
        break
if N < 0:
    N = N * -1
for i in range(1, N + 1):
    if N % i == 0:
        print(i, end=' ')
print()

# -----------------------------------------------= ЗАДАЧА 9 =-----------------------------------------------------------
# Проверьте, является ли введённое пользователем с клавиатуры натуральное число — простым.
# Постарайтесь не выполнять лишних действий (например, после того, как вы нашли хотя бы один нетривиальный делитель уже
# ясно, что число составное и проверку продолжать не нужно). Также учтите, что наименьший делитель натурального числа n,
# если он вообще имеется, обязательно располагается в отрезке [2; √n].
# ----------------------------------------------------------------------------------------------------------------------
'''
print()
print()
'''
# ----------------------------------------------= ЗАДАЧА 10 =-----------------------------------------------------------
# Создайте программу, выводящую на экран 12 первых элементов последовательности 2an-2–2, где a1=3 и a2=2.
# ----------------------------------------------------------------------------------------------------------------------
'''
print()
print()
'''
# ----------------------------------------------= ЗАДАЧА 11 =-----------------------------------------------------------
# Выведите на экран первые 11 членов последовательности Фибоначчи. Напоминаем, что первый и второй члены
# последовательности равны единицам, а каждый следующий — сумме двух предыдущих.
# ----------------------------------------------------------------------------------------------------------------------
'''
print()
print()
'''
# ----------------------------------------------= ЗАДАЧА 12 =-----------------------------------------------------------
# Для введённого пользователем с клавиатуры натурального числа посчитайте сумму всех его цифр (заранее не известно
# сколько цифр будет в числе).
# ----------------------------------------------------------------------------------------------------------------------
'''
print()
print()
'''
# ----------------------------------------------= ЗАДАЧА 13 =-----------------------------------------------------------
# В городе N проезд в трамвае осуществляется по бумажным отрывным билетам. Каждую неделю трамвайное депо заказывает в
# местной типографии рулон билетов с номерами от 000001 до 999999. «Счастливым» считается билетик у которого сумма
# первых трёх цифр номера равна сумме последних трёх цифр, как, например, в билетах с номерами 003102 или 567576.
# Трамвайное депо решило подарить сувенир обладателю каждого счастливого билета и теперь раздумывает, как много
# сувениров потребуется. С помощью программы подсчитайте сколько счастливых билетов в одном рулоне?
# ----------------------------------------------------------------------------------------------------------------------
'''
print()
print()
'''
# ----------------------------------------------= ЗАДАЧА 14 =-----------------------------------------------------------
# В городе N есть большой склад на котором существует 50000 различных полок. Для удобства работников руководство склада
# решило заказать для каждой полки табличку с номером от 00001 до 50000 в местной типографии, но когда таблички
# напечатали, оказалось что печатный станок из-за неисправности не печатал цифру 2, поэтому все таблички, в номерах
# которых содержалась одна или более двойка (например, 00002 или 20202) — надо перепечатывать.
# Напишите программу, которая подсчитает сколько всего таких ошибочных табличек оказалось в бракованной партии.
# ----------------------------------------------------------------------------------------------------------------------
'''
print()
print()
'''
# ----------------------------------------------= ЗАДАЧА 15 =-----------------------------------------------------------
# Электронные часы показывают время в формате от 00:00 до 23:59. Подсчитать сколько раз за сутки случается так, что
# слева от двоеточия показывается симметричная комбинация для той,что справа от двоеточия
# (например, 02:20, 11:11 или 15:51).
# ----------------------------------------------------------------------------------------------------------------------
'''
print()
print()
'''
# ----------------------------------------------= ЗАДАЧА 16 =-----------------------------------------------------------
# В американской армии считается несчастливым число 13, а в японской — 4. Перед международными учениями штаб российской
# армии решил исключить номера боевой техники, содержащие числа 4 или 13 (например, 40123, 13313, 12345 или 13040),
# чтобы не смущать иностранных коллег. Если в распоряжении армии имеется 100 тыс. единиц боевой техники и каждая боевая
# машина имеет номер от 00001 до 99999, то сколько всего номеров придётся исключить?
# ----------------------------------------------------------------------------------------------------------------------
'''
print()
print()
'''