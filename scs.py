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

print(scs(['GAT', 'CGA', 'TCG', 'GA', 'TCGA']))