"""
ID: corlan.1
LANG: PYTHON3
TASK: skidesign
"""

input = open('skidesign.in','r')
hills = int(input.readline())
elevs = [int(input.readline()) for _ in range(hills)]
input.close()

maxim,minim = max(elevs), min(elevs)
costs = []
for i in range(0, maxim - minim - 17 + 1):
    cost = 0
    newMin,newMax = (minim + i),(minim + i + 17)
    for e in elevs:
        if e < newMin:
            cost += (newMin - e)**2
            e = newMin
        if e > newMax:
            cost += (e - newMax)**2
            e = newMax
    costs.append(cost)

output = open('skidesign.out','w')
if len(costs) < 1: print(0, file=output)
else: print(min(costs),file=output)
output.close()
