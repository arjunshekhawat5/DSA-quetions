def num_sum(n, k):
    mtr = [[1]*(n+1) for _ in range(k+1)]

    for j in range(len(mtr)):
        for i in range(len(mtr[0])):
            if j <= 1:
                mtr[j][i] = j
            else:
                if i - j < 0:
                    mtr[j][i] = mtr[j-1][i]
                else:
                    mtr[j][i] = mtr[j-1][i] + mtr[j][i-j]
    for i in mtr:
        print(i)

    '''
    matrix = [[1]*(n+1) for _ in range(k+1)]
    for i in range(k+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                continue

            ans = matrix[i-1][j]
            a = i
            b = j
            while b > a:
                ans += matrix[i-1][b-a]
                b -= a

            matrix[i][j] = ans
    for i in matrix:
        print(i)

[1, 1, 1, 1, 1, 1]
[1, 1, 2, 3, 4, 5]
[1, 1, 2, 4, 6, 9]
[1, 1, 2, 4, 7, 11] '''


def main():
    print(num_sum(5, 3))


main()
