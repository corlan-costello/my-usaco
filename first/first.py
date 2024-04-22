"""
ID: corlan.1
LANG: PYTHON3
TASK: test
"""
with open("test.in","r") as fin:
    x,y = map(int, fin.readline().split())
    sum = x+y
fout = open ('test.out', 'w')
fout.write (str(sum) + '\n')
fout.close()