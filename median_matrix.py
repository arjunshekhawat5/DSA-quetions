def findMedian(A):
    row = []
    while len(A) > 0:
        temp = A.pop()
        row += temp
    return(row)


def findMedian_1(A):
    if len(A) == 1:
        return(A[0][len(A[0])//2])
    else:
        min_a, max_a = float('inf'), float("-inf")
        min_el = (len(A)*len(A[0]))/2
        for row in A:
            min_a = min(min_a, row[0])
            max_a = max(max_a, row[-1])

    while min_a < max_a:
        count, mid = 0,  (min_a + max_a)//2

        for row in A:
            if mid > row[-1]:
                count += len(row)
            else:
                for el in row:
                    if el <= mid:
                        count += 1
        if count <= min_el:
            min_a = mid + 1
        else:
            max_a = mid
    return(max_a)


print(findMedian_1([[1, 3, 5],
                    [2, 6, 9],
                    [3, 6, 9]]))
