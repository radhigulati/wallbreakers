def wordPattern(pattern, str):
    pD = {}
    sD = {}
    for i, val in enumerate(pattern):
        pD[val] = pD.get(val, []) + [i]

    for i, val in enumerate(str.split()):
        sD[val] = sD.get(val, []) + [i]

    return sorted(sD.values()) == sorted(pD.values())


print(wordPattern('abba', 'dog cat cat dog'))
print(wordPattern('abba', 'dog cat cat fish'))
print(wordPattern('aaaa', 'dog cat cat dog'))
print(wordPattern('abba', 'dog dog dog dog'))
