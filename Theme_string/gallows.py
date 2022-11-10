# ---------------------------= ИГРА   " Угадай слово по буквам" =------------------------------------------------------
# Загадали слово и напечатали - для каждой буквы
# У пользователя есть попытки  для угадывания (количество попыток определите сами, сообщите об этом пользователю)
# Пользователь вводит букву, вы сообщаете есть ли эта буква в слове или нет и показываете на каком она месте
# Если количество успешных попыток равно длине слова, то игра прекращается победой, и вы предлагаете пользователю
# ввести слово, или показываете ему слово, если он ввёл неправильное слово
# Если у пользователя закончились попытки, то поражение
#
# Дополнительно можно контролировать, если пользователь вводил уже такую букву, то не считать её успешной попыткой,
# а сообщить пользователю, что он теряет попытки,
# также если в слове  2 или более одинаковых  букв, то при успешной попытке тоже можно сообщить об этом пользователю


text = 'programmerimine'
answers = ''
count1 = 10
count2 = 0

print('Добро пожаловать в игру!')
print(f'Загаданное слово содержит {len(text)} букв')
print(f'У тебя есть {count1} попыток, чтобы отгадать')

zagadka = "_" * len(text)
print(zagadka)

while count1 != 0:
    zagadka = ''
    count2 += 1
    answer = input('Введите букву или слово целиком: ').lower()
    if len(answer) == len(text):
        if answer == text:
            print(f'Вы угадали за {count2} попыток')
        else:
            count1 -= 1
            print(f'Вы не угадали, у вас осталось {count1} попыток')
    elif len(answer) != 1 or answer.isalpha() == False:
        count1 -= 1
        print(f'Вы ввели что-то непонятное и потеряли попытку. Будьте внимательны, у вас осталось {count1} попыток')
    else:
        if answers.find(answer) != -1:
            count1 -= 1
            print(f'Вы уже отгадали эту букву и потеряли попытку. Будьте внимательны, у вас осталось {count1} попыток')
        elif text.find(answer) == -1:
            count1 -= 1
            print(f'Вы не угадали, у вас осталось {count1} попыток')
        else:
            answers = answers + answer


            for i in range(len(text)):
                if text[i] == answer:
                    zagadka += answer
                else:
                    zagadka += '_'
            print(zagadka)


