# ------------------------------------------------= ЗАДАЧА №4 =---------------------------------------------------------
# Реализуйте игру Крепс 
# ----------------------------------------------------------------------------------------------------------------------
# за основу взята статья https://habr.com/ru/post/411209/

import random


flag = True
while flag == True:
    print('Старт игры')

    point = 0
    # ход 1
    move = random.randint(1, 6) + random.randint(1, 6) #кидаем два кубика и суммируем выпавшие значения
    print(f'первый бросок, выпало {move}')
    if move == 7 or move == 11:
        flag = False
        print('Вы выиграли')
    elif move == 2 or move == 3 or move == 12:
        flag = False
        print('Вы проиграли')
    else:
        point = move   #Если выпадает другое число, оно запоминается под названием point

    # Если выпадает 7, то игрок проиграл. Если выпадает point то игрок выиграл. Если выпадают другие числа, ход повторяется
    count = 1
    flag = True
    while flag == True:
        count += 1
        move = random.randint(1, 6) + random.randint(1, 6)
        print(f'бросок номер {count}, выпало {move}')
        if move == 7:
            print('Вы проиграли')
            flag = False
        elif move == point:
            print('Вы выиграли')
            flag = False

print('Конец игры')