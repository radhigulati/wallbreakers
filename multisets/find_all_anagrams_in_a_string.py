from collections import Counter


def findAnangrams(s, p):
    res = []
    pattern = Counter(p)
    window_size = len(p)
    window = Counter(s[:window_size-1])
    for i in range(window_size-1, len(s)):
        c = s[i]
        window[c] += 1
        first_char_index = i-window_size+1
        first_char = s[i-window_size+1]
        if window == pattern:
            res.append(first_char_index)
        window[first_char] -= 1
        if window[first_char] == 0:
            del window[first_char]
    return res


print(findAnangrams('cbaebabacd', 'abc'))
