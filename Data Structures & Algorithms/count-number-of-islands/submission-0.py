class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        directions = [[1,0], [0,1], [-1, 0], [0, -1]]

        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                curRow, curCol = q.popleft()
                for dr, dc in directions:
                    newRow, newCol = dr + curRow, dc + curCol
                    if (newRow in range(ROWS) and newCol in range(COLS)
                       and grid[newRow][newCol] == "1" and
                       (newRow, newCol) not in visited):

                       q.append((newRow, newCol))
                       visited.add((newRow, newCol))
                



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands

        