code = input('Укажите свой код: ')
if code[0] in '2468':
    print("Пол: женский")
elif code[0] in '1357':
    print("Пол: мужской")

if code[0] in '12':
    print(f'Дата рождения: {code[5:7]}.{code[3:5]}.18{code[1:3]}')
if code[0] in '34':
    print(f'Дата рождения: {code[5:7]}.{code[3:5]}.19{code[1:3]}')
if code[0] in '56':
    print(f'Дата рождения: {code[5:7]}.{code[3:5]}.20{code[1:3]}')
if code[0] in '78':
    print(f'Дата рождения: {code[5:7]}.{code[3:5]}.21{code[1:3]}')

if int(code[7:10]) in range(1, 11):
    print("Больница Курессааре")
if int(code[7:10]) in range(11, 20):
    print("Женская клиника Тартуского университета")
if int(code[7:10]) in range(21, 151):
    print("Восточно-Таллиннская центральная больница, Родильный дом Пелгулинна (Таллинн)")
if int(code[7:10]) in range(151, 161):
    print("Больница Кейла")
if int(code[7:10]) in range(161, 221):
    print('Больница Рапла, Больница Локса, Больница Хийумаа (Кярдла)')

sum = 0

for i in range(len(code)-1):
    j = i + 1
    if j == 10:
        j = 1
    sum += int(code[i]) * j

if sum % 11 < 10:
    print(f"Контрольная цифра: {sum % 11}")
else:
    for i in range(len(code) - 1):
        j = i + 1
        if i >= 7:
            j = i - 6
        sum += int(code[i]) * j
    if sum % 11 < 10:
        print(f"Контрольная цифра: {sum % 11}")
    else:
        print(f"Контрольная цифра: 0")




