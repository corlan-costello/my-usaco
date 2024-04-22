"""
ID: corlan.1
LANG: PYTHON3
TASK: dualpal
"""

def base(number,base):
    exp = 0
    while base**(exp+1) <= number:
        exp += 1
    result = ''
    while exp >= 0:
        result += str(number//(base**exp))
        number = number%(base**exp)
        exp -= 1
    return result
# returns a string & base can't be greater than 10

input = open("dualpal.in","r")
N,S = input.readline().split()
N,S = int(N),int(S)

meet_req = []
n = S+1
while len(meet_req) < N:
    pals = 0
    for b in range(2,11):
        if base(n,b) == base(n,b)[::-1]:
            pals += 1
    if pals >= 2:
        meet_req.append(n)
    n += 1
output = open("dualpal.out",'w')
for i in meet_req:
    print(i,file=output)
