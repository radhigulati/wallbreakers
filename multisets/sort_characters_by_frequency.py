from collections import Counter


def frequencySort(s):
    res = ''
    for char, times in Counter(s).most_common():
        new = char * times
        res += new
    return res


print(frequencySort('tree'))
print(frequencySort('cccaaa'))
