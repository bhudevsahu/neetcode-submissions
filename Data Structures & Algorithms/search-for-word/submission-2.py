class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(r, c, i):            
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] != word[i] or
                (r, c) in visit
                
            ):
                return False
            
            if i+1 == len(word):
                return True
            
            visit.add((r, c))
            if (
                dfs (r+1, c, i+1) or
                dfs (r-1, c, i+1) or
                dfs (r, c+1, i+1) or
                dfs (r, c-1, i+1)
            ):
                return True

            visit.remove((r, c))

            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False
