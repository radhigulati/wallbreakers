# Current output for my version has extra spaces
def reverseWords(s):
    # new_s = list(s)
    # first = 0
    # for last in range(len(new_s)):
    #     if new_s[first] != ' ':
    #         last = first
    #         while last+1 < len(new_s) and new_s[last+1] != ' ':
    #             last += 1
    #         reverse_word(new_s, first, last)
    #         first = last + 1
    # return new_s
    new_s = list(s)
    first = 0
    for last in range(len(new_s)):
        if last == len(s) or s[last] == ' ':
            reverse_word(new_s, first, last)
            first = last + 1
    return ' '.join(new_s)


def reverse_word(new_s, first, last):
    while first <= last:
        new_s[first], new_s[last] = new_s[last], new_s[first]
        first += 1
        last -= 1
    # return ' '.join([word[::-1] for word in s.split(' ')])


print(reverseWords("Let's take LeetCode contest"))

# string to list ['L', 'e', 't', ''', 's']
# Reverse word
