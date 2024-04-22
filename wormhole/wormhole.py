"""
ID: corlan.1
LANG: PYTHON3
TASK: wormhole
"""

# return all possible pairings
def pairings(portals):
    ult_pairings = []
    if len(portals) < 2:
        return [[]]
    for p in portals[1:]:
        pair = [portals[0],p]
        portals1 = list(portals)
        portals1.remove(portals[0])
        portals1.remove(p)
        pairings1 = pairings(portals1)
        for pairing in pairings1:
            pairing.append(pair)
        ult_pairings += pairings1
    return ult_pairings

# coordinate's (wormhole's) "counterpart"
def counterpart(coord, pairing):
    for pair in pairing:
        if coord in pair:
            return pair[1 - pair.index(coord)]

def alignedCoord(coord, pairing):
    alignedCoords = []
    for pair in pairing:
        for c in pair:
            if c[1] == coord[1] and c[0] > coord[0]:
                alignedCoords.append(c)
    if len(alignedCoords) == 0:
        return False
    else:
        return min(alignedCoords)

# Determine if a certain pairing "loops"
def doesLoop(pairing):
    coords = [] # list of coordinates
    for pair in pairing:
        for coord in pair:
            coords.append(coord)
    # print(f"pairing: {pairing}")
    for coord in coords:
        initCoord = coord
        # print(f"initial: {initCoord}")
        currentCoord = initCoord
        for _ in range(len(coords)):
            # print(f"from {currentCoord} to {counterpart(currentCoord, pairing)} (cpart)")
            currentCoord = counterpart(currentCoord, pairing)
            # print(f"from {currentCoord} to {alignedCoord(currentCoord, pairing)} (aligned)")
            currentCoord = alignedCoord(currentCoord, pairing)
            if currentCoord == False:
                break
            if currentCoord == initCoord:
                # print(f"currentCoord = {currentCoord}")
                return True
    return False

input = open("wormhole.in","r")
N = int(input.readline())
coordinates = []
for _ in range(N):
    c = input.readline().split()
    for n in range(2):
        c[n] = int(c[n])
    coordinates.append(c)
# print(coordinates)
# print(pairings(coordinates))
loopPairings = 0
for p in pairings(coordinates):
    # print(doesLoop(p))
    if doesLoop(p):
        loopPairings += 1
output = open("wormhole.out", "w")
print(loopPairings, file=output)

