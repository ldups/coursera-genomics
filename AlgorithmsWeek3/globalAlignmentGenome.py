'''def editDistance(x, y):
    d = []
    for i in range(len(x) + 1):
        d.append([0] * (len(y) + 1))

    for i in range(1, len(x) + 1):
        d[i][0] = d[i-1][0] + 1
    for i in range(1, len(y) + 1):
        d[0][i] = d[0][i-1] + 1

    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            horizonDist = d[i][j-1] + 1
            verticalDist = d[i-1][j] + 1
            if x[i-1] == y[j-1]:
                diagDist = d[i-1][j-1]
            else:
                diagDist = d[i-1][j-1] + 1
            d[i][j] = min(horizonDist, verticalDist, diagDist)

    return d[-1][-1]'''

def findGlobalAlignment(p, genome):
    d = []
    # initialize arrary to 0s, first row remains all 0s
    for i in range(len(p) + 1):
        d.append([0] * (len(genome) + 1))

    #initialize first column to ascending numbers
    for i in range(1, len(p) + 1):
        d[i][0] = i

    for i in range(1, len(p) + 1):
        for j in range(1, len(genome) + 1):
            horizonDist = d[i][j-1] + 1
            verticalDist = d[i-1][j] + 1 
            if p[i-1] == genome[j-1]:
                diagDist = d[i-1][j-1]
            else:
                diagDist = d[i-1][j-1] + 1
            d[i][j] = min(horizonDist, verticalDist, diagDist)

    closestIndex = -1
    minDist = d[len(p)][0]
    for i in range(1, len(genome)):
        if d[len(p)][i] > minDist:
            minDist = d[len(p)][i]
            closestIndex = i

    return minDist, closestIndex
    




def readGenome(filename):
    genome = ''
    with open(filename, 'r')  as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome


'''filename = 'AlgorithmsWeek3\chr1.GRCh38.excerpt (1).fasta'
genome = readGenome(filename)'''

p = 'GCGTATGC'
t = 'TATTGGCTATACGGTT'

print(findGlobalAlignment(p, t))


