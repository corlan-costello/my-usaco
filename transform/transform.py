"""
ID: corlan.1
LANG: PYTHON3
TASK: transform
"""

import copy

def ninety_deg(square):
    square1 = copy.deepcopy(square)
    square1.reverse()
    rows1 = []
    for i in range(len(square1)):
        rows1.append([])
        for row in square1:
            rows1[-1].append(row[i])
    return rows1

def one_eighty_deg(square):
    return ninety_deg(ninety_deg(square))

def two_seventy_deg(square):
    return ninety_deg(one_eighty_deg(square))

def reflect(square):
    rows4 = copy.deepcopy(square)
    rows4.reverse()
    return one_eighty_deg(rows4)

def combo(square):
    return [ninety_deg(reflect(square)),one_eighty_deg(reflect(square)),two_seventy_deg(reflect(square))]

input = open("transform.in","r")
N = int(input.readline())
rows = []
for _ in range(N):
    r = []
    for character in input.readline().strip():
        r.append(character)
    rows.append(r)

new_rows = []
for _ in range(N):
    r = []
    for character in input.readline().strip():
        r.append(character)
    new_rows.append(r)

answer = '7'
if new_rows == ninety_deg(rows):
    answer += '1'
if new_rows == one_eighty_deg(rows):
    answer += '2'
if new_rows == two_seventy_deg(rows):
    answer += '3'
if new_rows == reflect(rows):
    answer += '4'
for x in combo(rows):
    if new_rows == x:
        answer += '5'
if new_rows == rows:
    answer += '6'
answer = min(answer)

output = open("transform.out","w")
print(answer,file=output)
