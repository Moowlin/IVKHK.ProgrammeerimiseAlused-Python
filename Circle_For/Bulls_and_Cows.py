print('Добро пожаловать в игру "Быки и коровы"')
print('ПРАВИЛА ИГРЫ:')
print('1. Компьютер загадывает четырехзначное число, в котором цифры не повторяются и ноль может стоять на первом месте')
print('2. Игрок пытается угадать загаданное число')
print('3. Компьютер дает ответ: количество коров и количество быков')
print('корова - угадано число, но позиция, бык - угадано и число, и позиция')
print()

def input_num_user():
    flag = True
    while flag == True:
        try:
            num_user = input('Ваш ответ: ')
            if num_user == '':
                flag = False
                return num_user
            if num_user.isdigit() == False or len(num_user) != 4: # не хватает проверки на аовторяемость цифр!
                raise Exception
        except Exception:
            print('Это недопустимое значение')
        else:
            flag = False
            return num_user
         
def checking_numbers(num_etalon, num_user):
    bull = 0
    cow = 0
    for i in range(len(num_etalon)):
        for j in range(len(num_user)):
            if num_etalon[i] == num_user[j] and i == j:
                bull += 1
            elif num_etalon[i] == num_user[j]:
                cow += 1
    return bull, cow
   

# ------------------------------------------------= НАЧАЛО ИГРЫ =--------------------------------------------------------
EndGame = False

while EndGame == False:
    print('Начинаем игру')
    print('Для завершения игры введите пустое значение')

    from random import randint

    num_etalon = ''
    while len(num_etalon) < 4:
        n = randint(0, 9)
        n = str(n)
        if n in num_etalon:
            continue
        else:
            num_etalon += n
    print('Я загадал число')
    print(num_etalon)

    guessing = False
    count = 0

    while guessing == False:
        num_user = input_num_user()
        if num_user == '':
            print('Куда же Вы? Останьтесь!')
            break
        count =+ 1
        bull, cow = checking_numbers(num_etalon, num_user)
        print(f'cow = {cow}, bull = {bull}')
        if bull == 4:
            print(f'Вы угадали за {count} попыток')
            guessing = True

    flag = True
    while flag == True:
        try:
            anwer = input(('Сыграем еще раз? Д/Н ')).upper()
            if anwer != 'Д' and anwer != 'Н':
                raise Exception
        except Exception:
            print()
        else:
            if anwer == "Д":
                print() 
                EndGame = False
                flag = False
            if anwer == "Н":
                EndGame = True
                flag = False

print('До скорой встречи!')         
