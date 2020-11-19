def sqrt(A):
    if A == 0 or A == 1:
        return A
    lo = 1
    hi = A//2
    while lo < hi:
        mid = (lo + hi)//2 + 1
        if mid*mid == A:
            return mid
        elif mid*mid < A:
            lo = mid
        else:
            hi = mid - 1
    return lo


for i in range(101):

    print(sqrt(i))
