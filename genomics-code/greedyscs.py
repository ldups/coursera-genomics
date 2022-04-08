from itertools import permutations
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

#test example
print(greedySCS(['ABC', 'BCA', 'CAB'], 1))