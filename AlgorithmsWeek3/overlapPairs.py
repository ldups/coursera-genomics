def overlap(a, b,  minLength):
    start = 0

    while True:
        start = a.find(b[:minLength], start)
        if start == -1:
            return 0

        if b.startswith(a[start:]):
            return len(a) - start #length of overlap
        start += 1

#print(overlap('TTACGT', 'CGTACCGT', 3))


from itertools import permutations

print(permutations(1, 2, 3), 1)

