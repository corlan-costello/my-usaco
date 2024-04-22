"""
ID: corlan.1
LANG: PYTHON3
TASK: namenum
"""
dictionary = open("dict.txt","r")
input = open("namenum.in","r")
serial = input.readline().strip()
touchtone = {
    "2":"ABC",
    "3":"DEF",
    "4":"GHI",
    "5":"JKL",
    "6":"MNO",
    "7":"PRS",
    "8":"TUV",
    "9":"WXY"
}
# "update" serial number
possibilities = []
for digit in serial:
    possibilities.append(touchtone[digit])
# make list of all names
names = []
for n in dictionary:
    n = n.strip()
    names.append(n)
# add correct names to a new empty list
valid_names = []
for n in names:
    valid = []
    if len(n) == len(serial):
        for i in range(len(n)):
            if n[i] in possibilities[i]:
                valid.append(True)
            else:
                valid.append(False)
        if False not in valid:
            valid_names.append(n)
# output correct names
output = open("namenum.out","w")
if len(valid_names) == 0:
    print("NONE",file=output)
else:
    for n in valid_names:
        print(n,file=output)
output.close()
