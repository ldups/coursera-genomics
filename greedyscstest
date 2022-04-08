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

def pick_maximal_overlap(reads, k, index):
    reada, readb = None, None
    best_olen = 0
    olen = 0
    for a in reads:
        matches = index[a[-k:]]
        for match in matches:
            if match != a:
                olen = overlap(a, match, k)
                if olen > best_olen:
                    reada, readb = a, match
                    best_olen = olen
    return reada, readb, best_olen

def greedySCS(reads, k):
    index = createIndex(reads, k)
    reada, readb, olen = pick_maximal_overlap(reads, k, index)
    while olen > 0:
        reads.remove(reada)
        reads.remove(readb)
        combinedRead = reada + readb[olen:]
        reads.append(reada + readb[olen:])
        updateIndex(reada, readb, combinedRead, index, k)
        reada, readb, olen = pick_maximal_overlap(reads, k, index)
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

def updateIndex(read1, read2, combRead, index, k):
    for seq in index:
        if read1 in index[seq]:
            index[seq].remove(read1)
        if read2 in index[seq]:
            index[seq].remove(read2)
    for i in range(len(combRead) - k + 1):
            kmer = combRead[i:i+k]
            if kmer not in index:
                index[kmer] = set()
            index[kmer].add(combRead)

#testing using course resources
filename = 'AlgorithmsWeek4\mysteryGenome.fq'
with open(filename, 'r') as opened_file:
    reads = parse_fastq(opened_file)

genome = greedySCS(reads, 30)
print('A', genome.count('A'))
print('T', genome.count('T'))
print('C', genome.count('C'))
print('G', genome.count('G'))