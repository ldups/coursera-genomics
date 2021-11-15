import bisect
import sys
class Index(object):
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

    def queryIndex(index, p, t):
        k = index.k
        offsets = []
        for i in index.query(p):
            #verification
            if p[k:] == t[i+k:i+len(p)]:
                offsets.append(i)
        return offsets

t = 'GCTACGATCTAGAATCTA'
p = 'TCTA'

index = Index(t, 2)
print(index.queryIndex(p, t))



