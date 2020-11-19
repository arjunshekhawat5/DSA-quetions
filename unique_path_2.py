def uniquePathsWithObstacles(grid):
    m = len(grid)
    n = len(grid[0])
    if grid[0][0] == 1:
        return 0
    else:
        grid[0][0] = 1
    for i in range(1, m):
        if grid[i][0] == 1:
            for j in range(i, m):
                grid[j][0] = 0
            break
        grid[i][0] = 1
    for i in range(1, n):
        if grid[0][i] == 1:
            for j in range(i, n):
                grid[0][j] = 0
            break
        grid[0][i] = 1

    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 1:
                grid[i][j] = 0
                continue
            grid[i][j] = grid[i-1][j] + grid[i][j-1]

    return grid[m-1][n-1]
