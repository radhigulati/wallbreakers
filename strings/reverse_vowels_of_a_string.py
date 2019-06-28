def reverseVowels(s):
    new_s = list(s)
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    first = 0
    last = len(new_s) - 1
    while first < last:
        while first < last and new_s[first] not in vowels:
            first += 1
        while last > first and new_s[last] not in vowels:
            last -= 1
        if new_s[first] in vowels and new_s[last] in vowels:
            new_s[first], new_s[last] = new_s[last], new_s[first]
        first += 1
        last -= 1
    return ''.join(new_s)


print(reverseVowels("hello"))
