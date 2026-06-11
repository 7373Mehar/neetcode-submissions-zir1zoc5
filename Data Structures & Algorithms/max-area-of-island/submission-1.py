class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(grid, curRow, curCol):
            if curRow < 0 or curCol < 0 or curRow == len(grid) or curCol == len(grid[curRow]) or grid[curRow][curCol] == 0:
                return 0

            # mark as visited
            grid[curRow][curCol] = 0

            return (1 + dfs(grid, curRow + 1, curCol) + dfs(grid, curRow, curCol + 1) + dfs(grid, curRow - 1, curCol) + dfs(grid, curRow, curCol - 1))


        rows = len(grid)
        columns = len(grid[0])
        res = 0

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    area = dfs(grid, i, j)
                    res = max(res, area)

        return res
                