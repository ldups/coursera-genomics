def readGenome(filename):
    genome = ''
    with open(filename, 'r')  as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

import dynamicEditDist

def globalAlignGenome(t, p):
    

















filename = 'AlgorithmsWeek3\chr1.GRCh38.excerpt (1).fasta'
genome = readGenome(filename)