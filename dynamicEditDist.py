def editDistance(x, y):
    d = []
    for i in range(len(x) + 1):
        d.append([0] * (len(y) + 1))
    for i in range(len(x) + 1):
        d[i][0] = i
    for i in range(len(y) + 1):
        d[0][i] = i

    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            horizonDist = d[i][j-1] + 1
            verticalDist = d[i-1][j] + 1
            if x[i-1] == y[j-1]:
                diagDist = d[i-1][j-1]
            else:
                diagDist = d[i-1][j-1] + 1
            d[i][j] = min(horizonDist, verticalDist, diagDist)

    return d[-1][-1]