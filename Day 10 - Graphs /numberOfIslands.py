class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands  = 0
        
        def dfs(r, c):
            # boundary check
            if (r not in range(ROWS) or 
            c not in range(COLS) or 
            (r, c) in visited or 
            grid[r][c] == "0"):
                return

            # mark vertex as visited 
            visited.add((r, c))

            # 4 edge direction 
            dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for dr, dc in dir:
                row, col = r + dr, c + dc 
                dfs(row, col)
                
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        return islands
        