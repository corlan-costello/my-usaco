"""
ID: corlan.1
LANG: PYTHON3
TASK: combo
"""

input = open('combo.in','r')
N = int(input.readline())

farmer_combo1 = input.readline().split()
farmer_combo = []
for n in farmer_combo1:
    farmer_combo.append(int(n))

master_combo1 = input.readline().split()
master_combo = []
for n in master_combo1:
    master_combo.append(int(n))

input.close()

def no_repeats(list):
    list.sort()
    list1 = []
    for l in range(len(list)):
        if l < len(list) - 1:
            if list[l] != list[l+1]:
                list1.append(list[l])
        else:
            list1.append(list[l])
    return list1


valid_farmer_combos = []
for n in farmer_combo:
    valid_positions = [(n-3)%N+1,(n-2)%N+1,(n-1)%N+1,n%N+1,(n+1)%N+1]
    valid_positions = no_repeats(valid_positions)
    valid_farmer_combos.append(valid_positions)

valid_master_combos = []
for n in master_combo:
    valid_positions = [(n-3)%N+1,(n-2)%N+1,(n-1)%N+1,n%N+1,(n+1)%N+1]
    valid_positions = no_repeats(valid_positions)
    valid_master_combos.append(valid_positions)

valid_combos = len(valid_farmer_combos[0])*len(valid_farmer_combos[1])*len(valid_farmer_combos[2]) + len(valid_master_combos[0])*len(valid_master_combos[1])*len(valid_master_combos[2])

common = [0,0,0]
for a in range(len(valid_farmer_combos)):
    for b in valid_farmer_combos[a]:
        if b in valid_master_combos[a]:
            common[a] += 1
valid_combos -= common[0]*common[1]*common[2]

output = open('combo.out','w')
print(valid_combos,file=output)
output.close()
