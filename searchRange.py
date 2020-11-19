def searchRange(A, B):
    lo = 0
    hi = len(A)
    while lo < hi:
        mid = (lo + hi)//2
        if A[mid] == B:
            start, end = mid, mid
            while True:
                if A[end + 1] == B:
                    end += 1
                else:
                    break
            while True:
                if A[start - 1] == B:
                    start -= 1
                else:
                    break
            return [start, end]
        elif A[mid] > B:
            hi = mid
        else:
            lo = mid + 1
    return [-1, -1]


def searchRange_1(A, B):
    lo = 0
    hi = len(A)
    while lo < hi:
        mid = (lo + hi)//2
        if A[mid] == B:
            start, end = mid, mid
            while end < len(A) - 1:
                if A[end + 1] == B:
                    end += 1
                else:
                    break
            while start > 0:
                if A[start - 1] == B:
                    start -= 1
                else:
                    break
            return [start, end]
        elif A[mid] > B:
            hi = mid
        else:
            lo = mid + 1
    return [-1, -1]


print(searchRange_1([1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5,
                     6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 4))
