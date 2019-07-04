from collections import Counter


def firstUniqChar(s):
    sD = Counter(s)
    for idx, letter in enumerate(s):
        if sD[letter] == 1:
            return idx
    return -1


print(firstUniqChar('leetcode'))
print(firstUniqChar('loveleetcode'))
