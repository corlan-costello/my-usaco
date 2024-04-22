"""
ID: corlan.1
LANG: PYTHON3
TASK: friday
"""

list = [0,0,0,0,0,0,0]
daysinmonth = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

def isleapyear(y):
    fate = True
    if y%400 == 0:
        fate = True
    elif y%100 == 0:
        fate = False
    elif y%4 == 0:
        fate = True
    else:
        fate = False
    return fate

thirteenth = 0
infile = open('friday.in','r')
N = int(infile.readline())
for year in range(1900,1900+N):
    for month in range(1,13):
        if isleapyear(year) == True and month == 3:
            thirteenth = (thirteenth + 29)%7
            list[thirteenth] += 1
        elif year == 1900 and month == 1:
            list[thirteenth] += 1
        elif year > 1900 and month == 1:
            thirteenth = (thirteenth + 31)%7
            list[thirteenth] += 1
        else:
            thirteenth = (thirteenth + daysinmonth[month-1])%7
            list[thirteenth] += 1

output = open('friday.out','w')
for number in range(6):
    output.write(f"{list[number]} ")
output.write(f"{list[6]}\n")
