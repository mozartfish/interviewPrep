class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited =  set() 
        totalIslands = 0
        # 4 way direction
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r, c):
            # base case and edge cases
            if (r not in range(ROWS) or 
            c not in range(COLS) or 
            (r, c) in visited or 
            grid[r][c] == "0"):
                return 
            
            # mark vertex as visited 
            visited.add((r, c))


            for dr, dc in dir:
                row = r + dr
                col = c + dc 
                dfs(row, col)
        
        # main algorithm 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    totalIslands += 1

        return totalIslands 