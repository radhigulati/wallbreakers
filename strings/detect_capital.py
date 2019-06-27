def detectCapitalUse(word):
    if word.isupper() or word.islower() or word.istitle():
        return True
    return False


print(detectCapitalUse('Radhika'))
print(detectCapitalUse('radhika'))
print(detectCapitalUse('RadhikA'))
