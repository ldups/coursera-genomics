def naive(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if t[i+j] != p[j]:
                match = False
                break
        if match:
            occurrences.append(i)
    return occurrences

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line [0] == '>':
                genome += line.rstrip()
    return genome

import random
def generateReads(genome, numReads, readLen):
    reads = []
    for _ in range(numReads):
        start = random.randint(0, len(genome) - readLen) - 1
        reads.append(genome[start: start + readLen])
    return reads

genome = readGenome('phix.fa')
reads = generateReads(genome, 100, 100)

numMatched = 0
for r in reads:
    matches = naive(r, genome)
    if len(matches) > 0:
        numMatched += 1
print('%d / %d reads matched exactly' % (numMatched, len(reads)))