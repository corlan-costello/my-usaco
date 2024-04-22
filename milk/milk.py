"""
ID: corlan.1
LANG: PYTHON3
TASK: milk
"""

input = open("milk.in","r")
N,M = input.readline().strip().split()
N,M = int(N),int(M)
farmers = []
for _ in range(M):
    i,j = input.readline().strip().split()
    farmers.append([int(i),int(j)])
input.close()

farmers.sort()
cost = 0
for f in farmers:
    cost += f[0]*f[1]
    N -= f[1]
    if N <= 0:
        cost += f[0]*N
        break

output = open("milk.out","w")
print(cost,file=output)
output.close()
