def intersection(nums1, nums2):
    intersectSet = set()
    newSet = set()

    for num in nums1:
        if num not in intersectSet:
            intersectSet.add(num)

    for num in nums2:
        if num in intersectSet:
            newSet.add(num)

    return newSet


print(intersection([1, 2, 2, 1], [2, 2]))
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
