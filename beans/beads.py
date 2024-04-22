"""
ID: corlan.1
LANG: PYTHON3
TASK: beads
"""

def collect_front(beads):
    color = None
    count = 0
    for bead in beads:
        if bead != 'w':
            if color == None:
                color = bead
            else:
                if bead != color:
                    return count
        count += 1
    return len(beads)

max_val = 0
input = open("beads.in","r")
N,necklace = int(input.readline()),input.readline().strip()
for i in range(len(necklace)):
    collection = collect_front(necklace) + collect_front(necklace[::-1])
    if collection > len(necklace):
        collection = len(necklace)
    if collection > max_val:
        max_val = collection
    necklace = necklace[1:] + necklace[0]
output = open("beads.out","w")
print(max_val,file=output)
