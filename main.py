from tabulate import tabulate

print("Use the following characters for corresponding propositional logic symbols:")
print("~ : NOT\n^ : AND\nv : OR\n=> : implies\n<=> : iff")
set = input("Enter set of propositional sentences: ")
letters = []
exp = [s for s in set.split(',')]
prev = False
for l in set:
    if l not in ',^<=>v' and l not in letters:
        if l == "~":
            prev = True
            continue
        if prev:
            letters.append("~"+l)
            prev = False
        else: letters.append(l)
        # print(letters)
rows = int(pow(2, len(letters)))
truthTable = {}
for index, l in enumerate(letters):
    repeat = len(letters)-1-index
    truthTable[l] = []
    b = True
    while len(truthTable[l]) != rows:
        if "~" in l:
            truthTable[l] = truthTable[l] + [not b for i in range(pow(2, repeat))]
        else:
            truthTable[l] = truthTable[l] + [b for i in range(pow(2, repeat))]
        b = not b
for e in exp:
    props = []
    symbol = []
    for l in e:
        if l == "~":
            prev = True
            continue
        if prev:
            l = "~"+l
            prev = False
        if l in letters:
            props.append(l)
    if "v" in e: symbol = "v"
    if "^" in e: symbol = "^"
    if "=>" in e: symbol = "=>"
    if "<=>" in e: symbol = "<=>"
    # print(props)
    # print(symbol)
    if symbol == "^":
        values = list(map(lambda x, y: x and y, truthTable[props[0]], truthTable[props[1]]))
    elif symbol == "v":
        values = list(map(lambda x, y: x or y, truthTable[props[0]], truthTable[props[1]]))
    elif symbol == "=>":
        values = list(map(lambda x, y: False if x and not y else True, truthTable[props[0]], truthTable[props[1]]))
    elif symbol == "<=>":
        values = list(map(lambda x, y: True if x == y else False, truthTable[props[0]], truthTable[props[1]]))

    truthTable[e] = values

print(tabulate(truthTable, headers='keys', tablefmt='fancy_grid', showindex=range(1, rows+1)))

models = []
for i in range(rows):
    cont = True
    interp = []
    for e in exp:
        if not truthTable[e][i]:
            cont = False
            break
    if cont:
        for letter in letters:
            if "~" in letter:
                interp.append(letter.replace('~','¬') if truthTable[letter][i] else letter.replace('~',''))
            else:
                interp.append(letter if truthTable[letter][i] else "¬"+letter)
            # print(interp)
        models.append(interp)
if len(models) > 0:
    print("The models of the propositional sentences are: ")
    for model in models:
        print("{" + ', '.join(model) + "}")
else:
    print("There are no models of these propositional sentences.")
# print(exp)
# print(letters)

# TEST CASES:
# AvB,A^C,C=>D
# Av~B,CvD