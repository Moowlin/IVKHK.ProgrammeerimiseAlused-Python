def createList(l, start, stop):
    from random import randint
    A = []
    for i in range(l):
        A.append(randint(start, stop))
    return A

print('7. ЗАДАЧА «ШЕРЕНГА»')
pupils = createList(10, 150, 160)
pupils.sort(reverse=True)
Peter = int(input('Укажите рост Пети: '))
print(f'Рост учеников: {pupils}')

for i in range(len(pupils)-1):
    if pupils[-1] >= Peter:
        print(f'Петя должен встать под номером {len(pupils)+1}')
        pupils.append(Peter)
        break
    if pupils[i] >= Peter > pupils[i+1]:
        print(f'Петя должен встать под номером {i+2}')
        pupils.insert(i+1, Peter)
        break
print(pupils)
print()