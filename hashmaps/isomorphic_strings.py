def isIsomorphic(s, t):
    sD = {}
    tD = {}

    for i, val in enumerate(s):
        sD[val] = sD.get(val, []) + [i]

    for i, val in enumerate(t):
        tD[val] = tD.get(val, []) + [i]

    return sorted(sD.values()) == sorted(tD.values())


print(isIsomorphic('egg', 'add'))
print(isIsomorphic('foo', 'bar'))
print(isIsomorphic('paper', 'title'))
