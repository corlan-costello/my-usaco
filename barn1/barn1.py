"""
ID: corlan.1
LANG: PYTHON3
TASK: barn1
"""

input = open('barn1.in','r')
num_of_boards,num_of_stalls,num_of_cows = input.readline().strip().split()
num_of_boards,num_of_stalls,num_of_cows = int(num_of_boards),int(num_of_stalls),int(num_of_cows)

occupied_stalls = []
for _ in range(num_of_cows):
    occupied_stalls.append(int(input.readline().strip()))

input.close()

occupied_stalls.sort()

spaces = []
for s in range(len(occupied_stalls)-1):
    spaces.append(occupied_stalls[s+1]-occupied_stalls[s])
for _ in range(num_of_cows-num_of_boards):
    spaces.remove(min(spaces))

length = 0
x = 0
while x <= len(occupied_stalls)-2:
    for space in spaces:
        if occupied_stalls[x+1] - occupied_stalls[x] == space:
            length += occupied_stalls[x] - occupied_stalls[0] + 1
            for _ in range(x+1):
                occupied_stalls.remove(occupied_stalls[0])
            x = -1
            spaces.remove(space)
    x += 1
length += occupied_stalls[-1] - occupied_stalls[0] + 1

output = open('barn1.out','w')
print(length,file=output)
output.close()
