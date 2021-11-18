import bisect
import readFASTA

class Index(object):
    #create and query index
    def __init__(self, t, k):
        self.k = k
        self.index = []
        for i in range(len(t) - k + 1):
            self.index.append((t[i:i+k], i))
        self.index.sort()
    
    def query(self, p):
        kmer = p[:self.k]
        i = bisect.bisect_left(self.index, (kmer, -1))
        hits = []
        while i < len(self.index):
            if self.index[i][0] != kmer:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits

    #'''def queryIndex(p, t, index):
     #   k = index.k
      #  offsets =  []
       # for i in index.query(p):
        #    if p[k:] == t[i+k:i+len(p)]:
         #       #verification
          #      offsets.append(i)
        #return offsets'''

def IndexQueryApprox(p, t, maxMismatch, kMerLen):
    index_o = Index(t, kMerLen)
    lenPartition = round(len(p) / (maxMismatch + 1))
    initialHits = []
    confirmedHits = set()

    for i in range(maxMismatch + 1):
        start = i*lenPartition
        if (i+1) * lenPartition < len(p):
            end = (i+1) * lenPartition
        else:
            end = len(p)
        partition = p[start:end]
        initialHits = index_o.query(partition)

        for hit in initialHits:
            #verification before partition
            numMisMatches = 0
            for j in range(0, start):
                if p[j] != t[hit - start + j]:
                    numMisMatches += 1
                if numMisMatches > maxMismatch:
                    break
            
            #verification after partition
            for j in range(end, len(p)):
                if p[j] != t[hit + start + end]:
                    numMisMatches += 1
                if numMisMatches > maxMismatch:
                    break

            if numMisMatches <= maxMismatch:
                confirmedHits.add(hit)

    return list(confirmedHits)

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

filename = 'chr1.GRCh38.excerpt.fasta'
genome = readFASTA.readGenome(filename)

p = 'GGCGCGGTGGCTCACGCCTGTAAT'

#print(genome)
print(IndexQueryApprox(p, genome, 2, 8))
print(naive_2mm(p, genome))