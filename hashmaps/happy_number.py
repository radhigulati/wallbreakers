def isHappy(n):
    seen = set()
    while n not in seen:
        seen.add(n)
        n = sum([int(num) ** 2 for num in str(n)])
    return n == 1


print(isHappy(19))
