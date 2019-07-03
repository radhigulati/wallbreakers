def uncommonFromSentences(A, B):
    uncommon = {}
    output = []
    for word in A.split():
        uncommon[word] = uncommon.get(word, 0) + 1
    for word in B.split():
        uncommon[word] = uncommon.get(word, 0) + 1
    return [word for word in uncommon if uncommon[word] == 1]


print(uncommonFromSentences('this apple is sweet', "this apple is sour"))
print(uncommonFromSentences('apple apple', 'banana'))
print(uncommonFromSentences('s z z s', 's z ejt'))
