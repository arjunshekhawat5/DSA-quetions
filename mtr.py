
def prettyPrint(A):
    result = []
    row = [A] * (2*A - 1)
    start = 0
    end = (2*A) - 1 
    while end - start >= 0:
        for i in range(start, end):
            row[i] = A
        temp = row[:]
        result.append(temp)
        A -= 1
        start += 1
        end -= 1
    result = result + result[::-1][1:]
    return result

print(prettyPrint(3))