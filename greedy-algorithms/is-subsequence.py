def isSubsequence(s, t):
    sidx = 0
    tidx = 0
    while sidx < len(s) and tidx < len(t):
        if s[sidx] == t[tidx]:
            sidx += 1
        tidx += 1

    return True if sidx == len(s) else False


print(isSubsequence('abc', 'ahbgdc'))
print(isSubsequence('axc', 'ahbgdc'))
