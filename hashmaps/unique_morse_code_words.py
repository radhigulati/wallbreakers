def uniqueMorseRepresentations(words):
    MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
             "....", "..", ".---", "-.-", ".-..", "--", "-.",
             "---", ".--.", "--.-", ".-.", "...", "-", "..-",
             "...-", ".--", "-..-", "-.--", "--.."]

    seen = set()
    for word in words:
        val = ''
        for s in word:
            val += MORSE[ord(s)-ord('a')]
        seen.add(val)
    return len(seen)


print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
