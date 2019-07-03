def distributeCandies(candies):
    return min(len(candies) / 2, len(set(candies)))


print(distributeCandies([1, 1, 2, 2, 3, 3]))
print(distributeCandies([1, 1, 2, 3]))
