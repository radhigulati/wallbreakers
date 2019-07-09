def isAnagram(s, t):
    return ''.join(sorted(s)) == ''.join(sorted(t))


print(isAnagram('anagram', 'nagaram'))
print(isAnagram('rat', 'car'))
