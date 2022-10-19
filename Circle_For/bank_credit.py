import math

laenu_summa = int(input('Сумма кредита: '))
P = int(input('Годовой процент: '))
aeg_kuudes = int(input('Время заёма (мес): '))

kuu_intress = P / 12 /100

laenumakse = round((laenu_summa * kuu_intress) / (1 - 1 / (math.pow((1 + kuu_intress), aeg_kuudes))), 2)

print('Periood', 'Laenu algjääk', 'Laenumakse', 'Intressmakse', 'Põhiosa tagasimakse', 'Laenu lõppjääk', sep="     ")

for i in range(1, aeg_kuudes + 1):
    intressmakse = round(laenu_summa * kuu_intress, 2)
    Voch = round(laenumakse - intressmakse, 2)
    ostatok_summ = round(laenu_summa - Voch, 2)
    print(i, laenu_summa, laenumakse, intressmakse, Voch, ostatok_summ, sep="            ")
    laenu_summa = ostatok_summ