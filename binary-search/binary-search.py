def search(nums, target):
    first = 0
    last = len(nums)-1
    while first <= last:
        mid = first + (last - first) // 2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return -1


print(search([-1, 0, 3, 5, 9, 12], 9))
