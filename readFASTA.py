def readGenome(filename):
    genome = ''
    with open(filename, 'r')  as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome