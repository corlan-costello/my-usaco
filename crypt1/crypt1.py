"""
ID: corlan.1
LANG: PYTHON3
TASK: crypt1
"""

input = open('crypt1.in','r')
num_of_digits = int(input.readline().strip())
digits1 = input.readline().split()
digits = []
for d in digits1:
    digits.append(int(d))
input.close()

solutions = 0
for factor1digit1 in digits:
    for factor1digit2 in digits:
        for factor1digit3 in digits:
            for factor2digit1 in digits:
                for factor2digit2 in digits:
                    factor1 = factor1digit1 * 100 + factor1digit2 * 10 + factor1digit3
                    factor2 = factor2digit1 * 10 + factor2digit2
                    if len(str(factor1 * factor2digit1)) == len(str(factor1 * factor2digit2)) == 3 and len(str(factor1 * factor2)) == 4:
                        nonfactors = str(factor1*factor2digit1) + str(factor1*factor2digit2) + str(factor1*factor2)
                        perfect = True
                        for x in nonfactors:
                            if int(x) not in digits:
                                perfect = False
                        if perfect == True:
                            solutions += 1

output = open("crypt1.out","w")
print(solutions,file=output)
output.close()
