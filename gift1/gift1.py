"""
ID: corlan.1
LANG: PYTHON3
TASK: gift1
"""
input = open('gift1.in','r')
NP = int(input.readline())
names = {}
for name in range(NP):
    names[input.readline()] = 0
for _ in range(NP):
    key = [input.readline(),input.readline()]
    dollars,people = key[1].split(' ')
    dollars = int(dollars)
    people = int(people)
    people1 = []
    for person in range(people):
        people1.append(input.readline())
    if people != 0:
        names[key[0]] -= (dollars - (dollars%people))
        for p in people1:
            names[p] += dollars//people
output = open('gift1.out','w')
for name in names:
    output.write(f"{name.strip()} {names[name]}\n")
