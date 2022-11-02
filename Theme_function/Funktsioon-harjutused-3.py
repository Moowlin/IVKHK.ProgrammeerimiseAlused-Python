# -----------------------------------------------------= Задача 3 =-----------------------------------------------------
# 3. Kirjuta funktsioon kuupäev_sõnena, mis võtab argumentideks päeva, kuu ja aasta (arvudena) ning tagastab sõne, mis
# esitab kuupäeva kujul <päev>. <kuu nimi> <aasta> (nt. 24. veebruar 1918). Seejärel kirjuta programm, mis küsib
# kasutajalt arvudena päeva, kuu ja aasta ning kuvab ekraanile vastava kuupäeva sõnena.

# 3. Напишите функцию в виде строки_даты, которая принимает день, месяц и год (в виде чисел) в качестве аргументов и
# возвращает строку, представляющую дату в форме <день>. <название месяца> <год> (например, 24 февраля 1918 г.). Затем
# напишите программу, которая запрашивает у пользователя день, месяц и год в виде чисел и отображает соответствующую
# дату на экране в виде слова.
# ----------------------------------------------------------------------------------------------------------------------

def months(n):
    match n:
        case 1: name = 'января'
        case 2: name ='февраля'
        case 3: name ='марта'
        case 4: name ='апреля'
        case 5: name ='мая'
        case 6: name ='июня'
        case 7: name ='июля'
        case 8: name ='августа'
        case 9: name ='сентября'
        case 10: name ='октября'
        case 11: name ='ноября'
        case 12: name ='декабря'
    return name


def date(day_month_year):
    day = day_month_year.split('_')[0]
    month = day_month_year.split('_')[1]
    year = day_month_year.split('_')[2]
    month = months(int(month))

    print(day, month, year,'г.')

def date_word(day_month_year):
    day = int(day_month_year.split('_')[0])
    month = int(day_month_year.split('_')[1])
    year = int(day_month_year.split('_')[2])
    month = months(month)


num = input('Введите дату день_месяц_год, например 1_1_1999: ')

date(num)
