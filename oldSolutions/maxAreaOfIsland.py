class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set() 
        area = 0 

        def dfs(r, c):
            if (r not in range(ROWS) or 
            c not in range(COLS) or 
            (r, c) in visited or 
            grid[r][c] == 0):
                return 0 
            
            # mark current node as visited
            visited.add((r, c))
            return 1 + dfs(r, c + 1) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    area = max(area, dfs(r, c))
        
        return area
        