from itertools import permutations

def overlap(a, b, k):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:k], start)  # look for b's prefix in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match

def parse_fastq(fh):
    """ Parse reads from a FASTQ filehandle.  For each read, we
        return a name, nucleotide-string, quality-string triple. """
    reads = []
    while True:
        first_line = fh.readline()
        if len(first_line) == 0:
            break  # end of file
        name = first_line[1:].rstrip()
        seq = fh.readline().rstrip()
        fh.readline()  # ignore line starting with +
        qual = fh.readline().rstrip()
        reads.append(seq)
    return reads
        
def createIndex(reads, k):
    index = {}
    for read in reads:
        for i in range(len(read) - k + 1):
            kmer = read[i:i+k]
            if kmer not in index:
                index[kmer] = set()
            index[kmer].add(read)
    return index

def findAllOverlaps(index, reads, k):
    matches = []
    numNodes = 0
    for read in reads:
        hasMatch = False
        suffix = read[-k:]
        prelimMatches = index[suffix]
        for ma in prelimMatches:
            if ma != read:
                overlapLen = overlap(read, ma, k)
                if overlapLen != 0:
                    matches.append([read, ma])
                    hasMatch = True
        if hasMatch:
            numNodes += 1
    return matches, numNodes

filename = 'AlgorithmsWeek3\ERR266411_1.for_asm.fastq'
fastq = open(filename)
reads = parse_fastq(fastq)
genomeDict = createIndex(reads, 30)

olaps = {}
for a,b  in permutations(reads, 2):
        overlapLen = overlap(a, b, 30)
        if overlapLen > 0:
            olaps[(a, b)] = overlapLen

print(len(olaps))


matches, numNodes = findAllOverlaps(genomeDict, reads, 30)
print(numNodes)
print(len(matches))


#reads = ['CGTACG', 'TACGTA', 'GTACGT', 'ACGTAC', 'GTACGA', 'TACGAT']
#genomeDict = createIndex(reads, 5)
#print(findAllOverlaps(genomeDict, reads, 5))