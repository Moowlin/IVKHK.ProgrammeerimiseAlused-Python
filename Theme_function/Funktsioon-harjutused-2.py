# -----------------------------------------------------= Задача 2 =-----------------------------------------------------
# 2. Kirjuta kõigepealt funktsioon, mis võtab argumendiks kuu numbri ja tagastab vastava kuu nime (väikeste tähtedega).
# Testi oma funktsiooni. Seejärel lisa programmi laused, mis küsivad kasutajalt kuu numbri ja väljastavad vastava kuu
# nime suurte tähtedega.

# 2. Сначала напишите функцию, которая принимает в качестве аргумента номер месяца и возвращает название
# соответствующего месяца (строчными буквами). Проверьте свою функцию. Затем добавьте операторы программы, которые
# запрашивают у пользователя номер месяца и выводят соответствующее название месяца заглавными буквами.
# ----------------------------------------------------------------------------------------------------------------------

def month(n):
    match n:
        case 1: name = 'январь'
        case 2: name ='февраль'
        case 3: name ='март'
        case 4: name ='апрель'
        case 5: name ='май'
        case 6: name ='июнь'
        case 7: name ='июль'
        case 8: name ='август'
        case 9: name ='сентябрь'
        case 10: name ='октябрь'
        case 11: name ='ноябрь'
        case 12: name ='декабрь'
    return name

num = int(input('Введите номер месяца: '))
print(month(num).upper())


