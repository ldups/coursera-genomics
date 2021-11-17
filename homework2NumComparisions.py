import bm_preproc
import readFASTA

#boyer moore search that returns num character comparisions and num alignments tried
def boyer_moore(p, p_bm, t):
    i = 0
    occurrences = []
    numCharComps = 0
    numAlignsTried = 0
    while i < len(t) - len(p) + 1:
        shift = 1
        mismatched = False
        numAlignsTried += 1
        for j in range(len(p) -1, -1, -1):
            numCharComps += 1
            if p[j] != t[i+j]:
                skip_bc = p_bm.bad_character_rule(j, t[i+j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True
                break
        if not mismatched:
            occurrences.append(i)
            skip_gs = p_bm.match_skip()
            shift = max(skip_gs, shift)
        i += shift
    return occurrences, numCharComps, numAlignsTried

#naive search that returns num character comparisions and num alignments tried
def naive(p, t):
    occurrences = []
    numCharComps = 0
    numAlignsTried = 0
    for i in range(len(t) - len(p) + 1):
        match = True
        numAlignsTried += 1
        for j in range(len(p)):
            numCharComps += 1
            if t[i+j] != p[j]:
                match = False
                break
        if match:
            occurrences.append(i)
    return occurrences, numCharComps, numAlignsTried


fileName = 'chr1.GRCh38.excerpt.fasta'
genome = readFASTA.readGenome(fileName)

p = 'GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG'
bm_o = bm_preproc.BoyerMoore(p, alphabet = 'ATCG')

occurencesBM, numCharsBM, numAlignsBM = boyer_moore(p, bm_o, genome)
#occurencesN, numCharsN,  numAlignsN = naive(p, genome)

#print('Naive chars:' + str(numCharsN) + '/nNaiveAligns:' + str(numAlignsN))
print('BM chars:' + str(numCharsBM) + '\nBMAligns:' + str(numAlignsBM))
