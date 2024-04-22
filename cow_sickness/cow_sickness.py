import sys

input = sys.stdin
cownum = int(input.readline().strip())
infections = input.readline().strip()

def toString(stringlist):
    r = ''
    for s in stringlist:
        r += s
    return r

def spread(combo):
    progress = [combo]
    while True:
        copy = combo
        combo = list(combo)
        copy = list(copy)
        for i in range(len(combo)):
            if copy[i] == '1':
                if i == 0:
                    combo[i+1] = '1'
                elif i == len(combo) - 1:
                    combo[i-1] = '1'
                elif i > 0 and i < len(combo) - 1:
                    combo[i+1] = '1'
                    combo[i-1] = '1'
        combo = toString(combo)
        progress.append(combo)
        if progress[-1] == progress[-2]:
            progress = progress[0:len(progress) - 1]
            break
    return progress

combos = []
for i in range( 0, int((10**(cownum) - 1)/9 + 1) ):
    c = str(i)
    b = True
    for digit in c:
        if digit != '0' and digit != '1':
            b = False
    if b == True:
        c = '0'*(cownum - len(c)) + c
        combos.append(c)

min_sick = cownum + 1
candidates = []
for combo in combos:
    if infections in spread(combo):
        candidates.append(combo)
        sick = 0
        for i in combo:
            if i == '1':
                sick += 1
        if sick < min_sick:
            min_sick = sick
output = sys.stdout
print(min_sick,file=output)
