def plusOne(digits):
    for num in range(len(digits)-1, -1, -1):
        if digits[num] < 9:
            digits[num] += 1
            return digits
        digits[num] = 0
    return [1] + digits


print(plusOne([1, 2, 3]))
print(plusOne([4, 3, 2, 1]))
print(plusOne([9, 9]))
