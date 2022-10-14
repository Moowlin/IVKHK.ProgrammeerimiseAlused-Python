print('Добро пожаловать в игру "Быки и коровы"')
print('ПРАВИЛА ИГРЫ:')
print('1. Компьютер загадывает четырехзначное число, в котором цифры не повторяются и ноль может стоять на первом месте')
print('2. Игрок пытается угадать загаданное число')
print('3. Компьютер дает ответ: количество коров и количество быков')
print('корова - угадано число, но позиция, бык - угадано и число, и позиция')

from random import randint

num_etalon = ''
while len(num_etalon) < 4:
    n = randint(0, 9)
    n = str(n)
    if n in num_etalon:
        continue
    else:
        num_etalon += n
print(num_etalon)

flag = True
while flag == True:
    try:
        num_user = input('Ваш ответ: ')
        if num_user.isdigit() == False or len(num_user) > 4: # не хватает проверки на аовторяемость цифр!
            raise Exception
    except Exception:
        print('Это недопустимое значение')
    else:
        flag = False

bull = 0
cow = 0

flag = True
while flag == True:
    for i in range(len(num_etalon)):
        for j in range(len(num_user)):
            if num_etalon[i] == num_user[j] and i == j:
                bull += 1
            elif num_etalon[i] == num_user[j]:
                cow += 1
    print(f'cow = {cow}, bull = {bull}')
    if bull == 4:
        flag = False

print('Вы угадали')
