import random
from re import M

'''locations = []
for i in range(8):
    locations.append([0 for x in range(8)])

states = []
for i in range(8):
    states.append([-1 for x in range(8)])

mineLocations = []
for i in range(10):
    randNum = random.randint(0,63)
    while randNum in mineLocations:
        randNum = random.randint(0,63)
    mineLocations.append(randNum)


mines = []
for i in range(8):
    mines.append([0 for x in range(8)])

for i in range(8):
    for j in range(8):
        if (i*8 + j) in mineLocations:
            mines[i][j]= True
        else:
            mines[i][j] = False'''

def isValidIndex(i,j):
    if i<0 or j<0:
        return False
    if i>3 or j>3:
        return False
    return True

states=[]
for i in range(3):
    states.append([-1 for x in range(3)])
mines = [[False,False,True],[True,False,False],[False,True,False]]
locations=[]
for i in range(3):
    locations.append([-1 for x in range(3)])

#find number of adjacent mines
for i in range(3):
    for j in range(3):
        if mines[i][j]:
            locations[i][j] = 'M'
        else:
            mineCount = 0
            if isValidIndex(i-1,j-1) and mines[i-1][j-1]:
                mineCount +=1
            if isValidIndex(i-1,j) and mines[i-1][j]:
                mineCount +=1
            if isValidIndex(i,j-1) and mines[i][j-1]:
                mineCount +=1
            if isValidIndex(i+1,j+1) and mines[i+1][j+1]:
                mineCount +=1
            if isValidIndex(i-1,j+1) and mines[i-1][j+1]:
                mineCount +=1
            if isValidIndex(i,j+1) and mines[i][j+1]:
                mineCount +=1
            if isValidIndex(i+1,j-1) and mines[i+1][j-1]:
                mineCount +=1
            if isValidIndex(i+1,j) and mines[i+1][j]:
                mineCount +=1
            locations[i][j] = mineCount

def recursiveReveal(i,j):
    if locations[i][j] == 'M':
        return
    if isValidIndex(i-1,j-1) and mines[i-1][j-1]:
        states(i-1,j-1) == 'R'
        recursiveReveal(i-1,j-1)
    if isValidIndex(i-1,j) and mines[i-1][j]:
        states(i-1,j) == 'R'
        recursiveReveal(i-1,j)
    if isValidIndex(i,j-1) and mines[i][j-1]:
        states(i,j-1) == 'R'
        recursiveReveal(i,j-1)
    if isValidIndex(i+1,j+1) and mines[i+1][j+1]:
        states(i+1,j+1) == 'R'
        recursiveReveal(i+1,j+1)
    if isValidIndex(i-1,j+1) and mines[i-1][j+1]:
        states(i-1,j+1) == 'R'
        recursiveReveal(i-1,j+1)
    if isValidIndex(i,j+1) and mines[i][j+1]:
        states(i,j+1) == 'R'
        recursiveReveal(i,j+1)
    if isValidIndex(i+1,j-1) and mines[i+1][j-1]:
        states(i+1,j-1) == 'R'
        recursiveReveal(i+1,j-1)
    if isValidIndex(i+1,j) and mines[i+1][j]:
        states(i+1,j) == 'R'
        recursiveReveal(i+1,j)



print(locations)
recursiveReveal(0,0)
print(states)





