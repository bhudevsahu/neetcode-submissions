class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        def dfs(r, c):
            if (
                r < 0
                or c < 0
                or r >= len(grid)
                or c >= len(grid[0])
                or grid[r][c] != "1"
            ):
                return
            grid[r][c] = "0"

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    num_islands += 1

        return num_islands