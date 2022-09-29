'''
• Дано целое число от 100 до 999. Вывести описание этого числа, например: 
256 - "двести пятьдесят шесть" 814 - "восемьсот четырнадцать"
'''

number = 0
while number not in range(100, 1000):
    number = int(input('введите число от 100 до 999 '))
    if number not in range(100, 1000):
        print('указано неверное число')
hundreds = number // 100
tens = number % 100 // 10
ones = number % 10

match hundreds:
    case 1: print('сто', end=' ')
    case 2: print('двести', end=' ')
    case 3: print('триста', end=' ')
    case 4: print('четыреста', end=' ')
    case 5: print('пятьсот', end=' ')
    case 6: print('шестьсот', end=' ')
    case 7: print('семьсот', end=' ')
    case 8: print('восемьсот', end=' ')
    case 9: print('девятьсот', end=' ')

if tens == 1 :
    match ones:
        case 0: print('десять', end=' ')
        case 1: print('одинадцать', end=' ')
        case 2: print('двенадцать', end=' ')
        case 3: print('тринадцать', end=' ')
        case 4: print('четырнадцать', end=' ')
        case 5: print('пятьнадцать', end=' ')
        case 6: print('шестьнадцать', end=' ')
        case 7: print('семьнадцать', end=' ')
        case 8: print('восемьнадцать', end=' ')
        case 9: print('девятьнадцать', end=' ')

match tens:
    case 2: print('двадцать', end=' ')
    case 3: print('тридцать', end=' ')
    case 4: print('сорок', end=' ')
    case 5: print('пятьдесят', end=' ')
    case 6: print('шестьдесят', end=' ')
    case 7: print('семьдесят', end=' ')
    case 8: print('восемьдесят', end=' ')
    case 9: print('девятносто', end=' ')   

if tens == 0 or tens in range(2,10):       
    match ones:
        case 1: print('один', end=' ')
        case 2: print('два', end=' ')
        case 3: print('три', end=' ')
        case 4: print('четыре', end=' ')
        case 5: print('пять', end=' ')
        case 6: print('шесть', end=' ')
        case 7: print('семь', end=' ')
        case 8: print('восемь', end=' ')
        case 9: print('девять', end=' ')  