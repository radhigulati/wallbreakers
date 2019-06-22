# my attempt
def sortArrayByParity(A):
    odd = []
    even = []
    for num in range(len(A)):
        if A[num] % 2 != 0:
            odd.append(A[num])
        else:
            even.append(A[num])
    return even+odd


print(sortArrayByParity([3, 1, 2, 4]))
