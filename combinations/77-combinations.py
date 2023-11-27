

def combine(n, k):
    combs = []
    helper(1, [], combs, n, k)
    return combs


def helper(i, curComb, combs, n, k):
    if len(combs) == k:
        combs.append(curComb.copy())

        return

    if i > n:
        return

    curComb.append(i)
    helper(i + 1, curComb, combs, n, k)
    curComb.pop()

    helper(i + 1, curComb, combs, n, k)
