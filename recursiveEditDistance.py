def edDistRecursive(a, b):
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    delt = 1 if a[-1] != b[-1] else 0
    return min(edDistRecursive(a[-1], b[-1]) + delt, edDistRecursive(a[-1], b) + 1, edDistRecursive(a, b[-1]) + 1)

#example used for testing
print(edDistRecursive('Hello', 'helloj'))