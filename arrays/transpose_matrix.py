def transpose(A):
    # for transposing, switch rows and columns
    R = len(A)
    C = len(A[0])
    ans = [[None] * R for _ in range(C)]
    for r, row in enumerate(A):
        for c, val in enumerate(row):
            ans[c][r] = val
    return ans


print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(transpose([[1, 2, 3], [4, 5, 6]]))
