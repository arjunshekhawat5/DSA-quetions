class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.total_paths = 0
        total_zeros = 0

        def dfs(i, j, grid, total_zeros):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == -1 or (grid[i][j] == 2 and total_zeros != 0) or grid[i][j] == 5:
                return
            temp = grid[i][j]
            if grid[i][j] == 2 and total_zeros == 0:
                self.total_paths += 1
            if grid[i][j] == 0:
                total_zeros -= 1
            grid[i][j] = 5

            dfs(i - 1, j, grid, total_zeros)
            dfs(i, j-1, grid, total_zeros)
            dfs(i+1, j, grid, total_zeros)
            dfs(i, j + 1, grid, total_zeros)

            grid[i][j] = temp

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    total_zeros += 1
        print(total_zeros)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    dfs(i, j, grid, total_zeros)
        return self.total_paths
