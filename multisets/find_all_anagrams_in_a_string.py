from collections import Counter


def findAnagrams(s, p):
    # create an empty array
    res = []
    # add all letters in p to dictionary
    pCounter = Counter(p)
    # add all letters in s starting from index 0 to len(p)-1 to dictionary
    sCounter = Counter(s[:len(p)-1])
    # for i from len(p)-1 to len(s)
    for i in range(len(p)-1, len(s)):
        # include a new char in the window (s dictionary)
        sCounter[s[i]] += 1
        # if sCounter and pCounter are the same
        # This step is O(1), since there are at most 26 English letters
        if sCounter == pCounter:
            # append the starting index which is found by
            res.append(i-len(p)+1)
        # decrease the count of oldest char in the window
        sCounter[s[i-len(p)+1]] -= 1
        if sCounter[s[i-len(p)+1]] == 0:
            del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
    return res


print(findAnagrams('cbaebabacd', 'abc'))
print(findAnagrams('abab', 'ab'))
