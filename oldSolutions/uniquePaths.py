class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n 
        cache = {} 
        for r in range(ROWS):
            for c in range(COLS):
                cache[(r, c)] = 0 
        
        def dp(r, c, ROWS, COLS, cache):
            if r == ROWS or c  == COLS:
                return 0 
            if cache[(r, c)] > 0:
                return cache[(r, c)]
            if r == ROWS - 1 and c == COLS - 1:
                return 1 
            cache[(r, c)] = dp(r + 1, c, ROWS, COLS, cache) + dp(r, c + 1, ROWS, COLS, cache)
            return cache[(r, c)]
        
        return dp(0, 0, ROWS, COLS, cache)
        