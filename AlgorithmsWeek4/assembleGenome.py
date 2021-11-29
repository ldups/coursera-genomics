from itertools import permutations

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

def overlap(a, b,  minLength):
    start = 0

    while True:
        start = a.find(b[:minLength], start)
        if start == -1:
            return 0

        if b.startswith(a[start:]):
            return len(a) - start #length of overlap
        start += 1

def scs(ss):
    shortest_sup = None
    for ssperm in permutations(ss):
        sup = ssperm[0]
        for i in range(len(ss) - 1):
            olen = overlap(ssperm[i], ssperm[i+1], 1)
            sup += ssperm[i+1][olen:]
        if shortest_sup is None or len(sup) < len(shortest_sup):
            shortest_sup = sup
    return shortest_sup

def pick_maximal_overlap(reads, k):
    reada, readb = None, None
    best_olen = 0
    olen = 0
    for a, b in permutations(reads, 2):
        olen = overlap(a, b, 1)
        if olen > best_olen:
            reada, readb = a, b
            best_olen = olen
    return reada, readb, olen

def greedySCS(reads, k):
    reada, readb, olen = pick_maximal_overlap(reads, k)
    while olen > 0:
        reads.remove(reada)
        reads.remove(readb)
        reads.append(reada + readb[olen:])
        reada, readb, olen = pick_maximal_overlap(reads, k)
    return ''.join(reads)

def createIndex(reads, k):
    index = {}
    for read in reads:
        for i in range(len(read) - k + 1):
            kmer = read[i:i+k]
            if kmer not in index:
                index[kmer] = set()
            index[kmer].add(read)
    return index

filename = 'AlgorithmsWeek4\mysteryGenome.fq'
with open(filename, 'r') as opened_file:
    reads = parse_fastq(opened_file)

genome = greedySCS(reads, 30)
#print('A', genome.count('A'))
#print('T', genome.count('T'))
#print('C', genome.count('C'))
#print('G', genome.count('G'))