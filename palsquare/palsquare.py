"""
ID: corlan.1
LANG: PYTHON3
TASK: palsquare
"""

def base(number,base):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    largest_exp = 0
    while True:
        if number%(base**(largest_exp+1)) == number:
            break
        largest_exp += 1

    new_number = ''
    for x in range(largest_exp+1):
        digit = number//(base**(largest_exp-x))
        if digit > 9:
            new_number += alphabet[digit-10]
        elif digit <= 9:
            new_number += str(digit)
        number = number%(base**(largest_exp-x))

    return new_number

def reverse(num):
    reversed_num = ''
    for i in range(len(num)):
        reversed_num += num[-1-i]
    return reversed_num

input = open("palsquare.in","r")
B = int(input.readline().strip())
output = open("palsquare.out","w")
for N in range(1,301):
    if base(N**2,B) == reverse(base(N**2,B)):
        print(base(N,B),base(N**2,B),file=output)

output.close()
