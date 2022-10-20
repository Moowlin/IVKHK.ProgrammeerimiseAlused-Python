# ------------------------------------------------= ЗАДАЧА №4 =---------------------------------------------------------
# Реализуйте игру Крепс 
# ----------------------------------------------------------------------------------------------------------------------
# за основу взята статья https://habr.com/ru/post/411209/

import random

def add_bet(wallet):
    flag = True
    while flag == True:
        try: 
            bet = int(input('Укажите вашу ставку: '))
            if bet not in range(1, wallet+1):
                raise Exception
        except Exception:
            print('Это недопустимое значение')
        else:
            flag = False
            return bet


def round_game(wallet, win, loss):
    flag = True
    while flag == True:
        print('Старт раунда')
        bet = add_bet(wallet)
        point = 0

        # ход 1
        move = random.randint(1, 6) + random.randint(1, 6) #кидаем два кубика и суммируем выпавшие значения
        print(f'первый бросок, выпало {move}')
        if move == 7 or move == 11:
            flag = False
            wallet += bet
            win = 1
            print('Вы выиграли')
        elif move == 2 or move == 3 or move == 12:
            wallet -= bet
            loss = 1
            flag = False
            print('Вы проиграли')
        else:
            point = move   #Если выпадает другое число, оно запоминается под названием point

        # Если выпадает 7, то игрок проиграл. Если выпадает point то игрок выиграл. Если выпадают другие числа, ход повторяется
        count = 1
        while flag == True:
            count += 1
            move = random.randint(1, 6) + random.randint(1, 6)
            print(f'бросок номер {count}, выпало {move}')
            if move == 7:
                wallet -= bet
                loss = 1
                print('Вы проиграли')
                flag = False
            elif move == point:
                wallet += bet
                win = 1
                print('Вы выиграли')
                flag = False

    print('Конец раунда')
    print('Итоги:')
    print(f'Состояние кошелька {wallet} евро')
    return wallet, win, loss

def question():
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
                return EndGame
            if anwer == "Н":
                EndGame = True
                flag = False
                return EndGame

# ------------------------------------------------= Игра =---------------------------------------------------------
EndGame =  False
wallet = 100
win = 0
loss = 0
sum_win = 0
sum_loss = 0

while EndGame ==  False:
    print(f'В вашем кошельке {wallet} евро')
    wallet, win, loss = round_game(wallet, win, loss)
    sum_win += win
    sum_loss += loss

    print(f'всего выиграшей {sum_win}, проигрышей {sum_loss}')
    if wallet <= 0:
        print('Вы банкрот 🤣')
        EndGame ==  True
        break
    else:
        EndGame = question()