'''
4 <- maxSum			12 <- maxSum
1	1	1			2	2	2
1	1	1			3	3	3
1	1	1			4	4	4
                    [[2, 4,   6],
                     [5, 10, 15], 
                     [9, 18, 27]]
'''

# Given a square matrix of integers and a maxSum variable you have to output max k where all k*k matrices has sum less then maxSum


def main():
    arr = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]
    max_sum = 12
    sum_arr = sum_ar(arr)
    print(sum_arr)
    for i in range(len(arr)):
        if sum_arr[i][i] > max_sum:
            print(i)
            break


def sum_ar(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                print(arr[i][j-1], arr[i])
                arr[i][j] = arr[i][j-1] + arr[i][j]
            elif j == 0:
                arr[i][j] = arr[i-1][j] + arr[i][j]
            else:
                arr[i][j] = arr[i][j-1] + \
                    arr[i-1][j] + arr[i][j] - arr[i-1][j-1]

    return arr


main()
