slova = dict()
text = 'one two one tho three'
arr = text.split(" ")
for e in arr:
    if e in slova:
        slova[e] += 1
    else:
        slova[e] = 1
for key in slova:
    print(key, 'встречается', slova[key], 'раза')