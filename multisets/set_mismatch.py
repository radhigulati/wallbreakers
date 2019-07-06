def findErrorNums(nums):
    new = set(nums)
    n = len(new)
    total = (n+1)*(n+2)//2
    missing = total-sum(new)
    return missing


print(findErrorNums([1, 2, 2, 4]))
