
def solution(a, b):
    i, j = 0, 0
    res = []
    while i < len(a) and j < len(b):
        res.append(a[i])
        res.append(b[i])
        i += 1
        j += 1

    res.append(a[i:])
    res.append(b[j:])

    return "".join(res)


def solutionString(a, b):
    i, j = 0, 0
    res = ""

    while i < len(a) and j < len(b):
        res += a[i]
        res += b[i]
        i += 1
        j += 1

    res += a[i:]
    res += b[j:]

    return res


