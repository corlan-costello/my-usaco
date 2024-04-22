import sys

input = sys.stdin
cownum,candynum = input.readline().strip().split()
cownum,candynum = int(cownum), int(candynum)
cow_heights = input.readline().strip().split()
for i in range(len(cow_heights)):
    cow_heights[i] = int(cow_heights[i])
candy_heights = input.readline().strip().split()
for i in range(len(candy_heights)):
    candy_heights[i] = int(candy_heights[i])

for candy_height in candy_heights:
    air_height = 0
    for h in range(len(cow_heights)):
        if cow_heights[h] > air_height:
            if cow_heights[h] < candy_height:
                c = cow_heights[h]
                cow_heights[h] += cow_heights[h] - air_height
                air_height = c
            else:
                cow_heights[h] += candy_height - air_height
                air_height = candy_height

output = sys.stdout
for height in cow_heights:
    print(height,file=output)
