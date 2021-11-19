def readFASTQ(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()
            seq = fh.readline()
            fh.readline()
            qual = fh.readline()
            sequences.append(seq.rstrip())
            qualities.append(qual.rstrip())