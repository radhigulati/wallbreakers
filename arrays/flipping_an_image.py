def flipAndInvertImage(A):
  # If the elements are the same, we can go ahead and invert them!
    for row in A:
        j, k = 0, len(row)-1
        while j <= k:
            if row[j] == row[k]:
                row[j], row[k] = row[j] ^ 1, row[k] ^ 1
            j += 1
            k -= 1
    return A


print(flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
print(flipAndInvertImage(
    [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
