def uniquePaths(m: int, n: int):
    a = [[0]*n] * m
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                a[i][j] = 1
            else:
                a[i][j] = a[i-1][j] + a[i][j-1]

    return a[m-1][n-1]


'''
[1,1,1]
[1,1+1,0]
[1,0,0]

mtr = [[0]*m for _ in range(n)]

fill the first row and coloumn with 1
iterate over over every value of the matrix
if first row or first coloumn cell = 1
value of the cell = value of the cell above + value of cell left to it

return last value of the matrix
'''


def unique_path(n, m):
    path = [[1]*m for _ in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            path[i][j] = path[i-1][j] + path[i][j-1]

    return path[n-1][m-1]


print(unique_path(3, 7), uniquePaths(3, 7))




