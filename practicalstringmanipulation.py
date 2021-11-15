import random

seq = ''
for _ in range(10):
    seq += random.choice('ACGT')
print(seq)

seq = ''.join([random.choice('ACGT')for _ in range(10)])
print(seq)

def longestCommonPrefix(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    return s1[:i]

def reverseComplement(seq1):
    complement = {'A': 'T', 'C': 'G', 'G':'C', 'T':'A'}
    returnSeq = ''
    for char in seq1:
        returnSeq = complement[char] +  returnSeq
    return returnSeq

print(reverseComplement('ATCG'))