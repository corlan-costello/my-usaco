"""
ID: corlan.1
LANG: PYTHON3
TASK: ride
"""
alphabet = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def convert(string):
    string = string.strip()
    string_number = 1
    for letter in string:
        string_number *= alphabet.find(letter)
    return string_number%47

names = open('ride.in','r')
comet,group = names.readlines()
output = open('ride.out','w')
result = "GO\n" if convert(comet) == convert(group) else "STAY\n"
output.write(result)
names.close()
output.close()
