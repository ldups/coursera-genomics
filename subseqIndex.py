import bisect
import readFASTA

class SubseqIndex(object):
    """ Holds a subsequence index for a text T """
    
    def __init__(self, t, k, ival):
        """ Create index from all subsequences consisting of k characters
            spaced ival positions apart.  E.g., SubseqIndex("ATAT", 2, 2)
            extracts ("AA", 0) and ("TT", 1). """
        self.k = k  # num characters per subsequence extracted
        self.ival = ival  # space between them; 1=adjacent, 2=every other, etc
        self.index = []
        self.span = 1 + ival * (k - 1)
        for i in range(len(t) - self.span + 1):  # for each subseq
            self.index.append((t[i:i+self.span:ival], i))  # add (subseq, offset)
        self.index.sort()  # alphabetize by subseq
    
    def query(self, p):
        """ Return index hits for first subseq of p """
        subseq = p[:self.span:self.ival]  # query with first subseq
        i = bisect.bisect_left(self.index, (subseq, -1))  # binary search
        hits = []
        while i < len(self.index):  # collect matching index entries
            if self.index[i][0] != subseq:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits

def querySubSeqIndex(t, p, k, ival, maxMismatch):
    subseqO = SubseqIndex(t, k, ival)
    confirmedHits = set()
    totalIndexHits = 0
    
    for i in range(0, min(int(len(p)/k), len(p))):
        initialHits = subseqO.query(p[i:])
        
        for hit in initialHits:
            numMisMatches = 0
            totalIndexHits += 1
            #verification before start
            for j in range(0, i):
                if not p[j] == t[hit - i + j]:
                    numMisMatches += 1
                if numMisMatches > maxMismatch:
                    break

            #verification after start
            for j in range(i + 1, len(p)):
                if not j - i % ival == 0:
                    if not p[j] == t[hit - i + j]:
                        numMisMatches += 1
                    if numMisMatches > maxMismatch:
                        break

            if numMisMatches <= maxMismatch:
                confirmedHits.add(hit-i)

    return list(confirmedHits), totalIndexHits

#testing using course resources
filename = 'chr1.GRCh38.excerpt.fasta'
genome = readFASTA.readGenome(filename)
p = 'GGCGCGGTGGCTCACGCCTGTAAT'

indexResult, totalHits = querySubSeqIndex(genome, p, 8, 3, 2)
indexResult.sort()
print(indexResult, totalHits)
