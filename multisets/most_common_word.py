from collections import Counter


def mostCommonWord(paragraph, banned):
    res = 0
    main = None
    d = {}
    for c in ",?!';:.":
        paragraph = paragraph.replace(c, ' ').lower()
    newPar = paragraph.split()
    parCounter = Counter(newPar)
    for i in newPar:
        if i in banned:
            parCounter[i] -= 1
    for k, v in parCounter.items():
        if v > res:
            res = v
            main = k
    return main


print(mostCommonWord(
    "Bob hit a ball, the hit BALL flew far after it was hit.", ['hit']))
