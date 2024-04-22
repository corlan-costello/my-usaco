"""
ID: corlan.1
LANG: PYTHON3
TASK: milk2
"""

input = open("milk2.in","r")
N = int(input.readline())
ordered = []
for _ in range(N):
    start,end = input.readline().split()
    start,end = int(start),int(end)
    ordered.append([start,end])
ordered.sort()
cont_min,cont_max = ordered[0][0],ordered[0][1]
cont = [cont_max - cont_min]
idle = [0]
for list in ordered:
    if cont_min <= list[0] <= cont_max <= list[1]:
        cont_max = list[1]
    cont.append(cont_max - cont_min)
    if cont_max < list[0]:
        idle.append(list[0] - cont_max)
        cont_min,cont_max = list[0],list[1]
output = open('milk2.out','w')
print(f"{max(cont)} {max(idle)}",file=output)
