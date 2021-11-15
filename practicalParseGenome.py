filename = 'lambda_virus.fa'
def readGenome(filename):
    genome = ''
    with open(filename, 'r')  as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

def numBases(genome):
    counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for base in genome:
        counts[base] +=1
    return counts

import collections
print(collections.Counter(readGenome(filename)))  

print(numBases(readGenome(filename)))

