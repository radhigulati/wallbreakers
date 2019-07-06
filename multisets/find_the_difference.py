from collections import Counter


def findTheDifference(s, t):
    newS = Counter(s)
    #newT = Counter(t)
    for i in t:
        if i in newS:
            newS[i] -= 1
        else:
            newS[i] += 1

    for k, v in newS.items():
        if v > 0 or v < 0:
            return k
    return None


print(findTheDifference('abcd', 'abcde'))
print(findTheDifference('a', 'aa'))
