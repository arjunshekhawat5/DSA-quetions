total_paths = 0


# dfs approach has runtime of 2**(m+n) which is very slow for large input
def uniquePaths(m, n):
    i, j = 0, 0

    def dfs(i, j, m, n):
        global total_paths
        # if i or j is out of bounds or i and j are m,n
        if i >= m or j >= n:
            return
        if (i, j) == (m - 1, n - 1):
            total_paths += 1
        dfs(i + 1, j, m, n)
        dfs(i, j + 1, m, n)
    dfs(i, j, m, n)
    return total_paths


print(uniquePaths(23, 12))
