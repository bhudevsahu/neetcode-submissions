class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(h), len(h[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visit or
                h[r][c] < prevHeight
            ):
                return

            visit.add((r, c))
            dfs(r+1, c, visit, h[r][c])
            dfs(r-1, c, visit, h[r][c])
            dfs(r, c+1, visit, h[r][c])
            dfs(r, c-1, visit, h[r][c])
    
        for c in range(COLS):
            dfs(0, c, pac, h[0][c])
            dfs(ROWS-1, c, atl, h[ROWS-1][c])
            
        for r in range(ROWS):
            dfs(r, 0, pac, h[r][0])
            dfs(r, COLS - 1, atl, h[r][COLS-1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
