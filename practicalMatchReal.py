def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line [0] == '>':
                genome += line.rstrip()
    return genome

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

def naiveStrandAware(p, t):
    if p == reverseComplement(p):
        return naive(p,  t)
    occurrences =  naive(p, t)
    occurrences.extend(naive(reverseComplement(p), t))
    return occurrences

def naive_2mm(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        numMM = 0
        match = True
        for j in range(len(p)):
            if t[i+j] != p[j]:
                numMM += 1
            if numMM > 2:
                match = False
                break
        if match:
            occurrences.append(i)
    return occurrences

def readFASTQ(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()
            seq = fh.readline().rstrip()
            fh.readline()
            qual = fh.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities

def reverseComplement(seq1):
    complement = {'A': 'T', 'C': 'G', 'G':'C', 'T':'A', 'N': 'N'}
    returnSeq = ''
    for base in seq1:
        returnSeq = complement[base] +  returnSeq
    return returnSeq

def phred33toQ(phred):
    return ord(phred) -  33

def QtoPhred33(q):
    return chr(q + 33)

def findAvQuality(qualities):
    posDict = {}
    posValues = {}
    for str in qualities:
        for i in range(len(str)):
            phred = str[i]
            q = phred33toQ(phred)
            if i in posDict:
                posDict[i][0] += q
                posDict[i][1] += 1
            else:
                posDict[i] = [q, 1]
    for index in posDict:
        posValues[index] = posDict[index][0] / posDict[index][1]
    return posValues

def lowestQual(qualities):
    posValues = findAvQuality(qualities)
    lowestQual = 
    lowestIndex = 0
    for pos in posValues:
        if posValues[pos] < :
            lowestQual = posValues[pos]
            lowestIndex = pos
    return lowestIndex




humReads, humQualities = readFASTQ('ERR037900_1.first1000.fastq')
genome = readGenome('lambda_virus.fa')
print(findAvQuality(humQualities))






#numMatched = 0
#n = 0
#for r in phix_reads:
#    r = r[:10]
#    matches = naive(r, genome)
#    matches.extend(naive(reverseComplement(r), genome))
#    n += 1
#    if len(matches) > 0:
#        numMatched += 1

#print('%d / %d reads matched exactly' % (numMatched, n))
#print(len(naiveStrandAware('TTAA', genome)))
#print(len(naive('TTAA', genome)))
#print(len(naive(reverseComplement('TTAA'), genome)))
#print(naive_2mm('AGGAGGTT', genome))