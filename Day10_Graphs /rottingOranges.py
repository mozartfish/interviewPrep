class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque 
        ROWS, COLS = len(grid), len(grid[0])
        q = deque() 
        visited = set() 
        time = 0
        fresh = 0 

        # count fresh oranges 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1 
                if grid[r][c] == 2:
                    q.append([r, c])
        # figure out the directions
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # BFS Algorithm
        while len(q) > 0 and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dir:
                    row, col = r + dr, c + dc
                    # check boundary condition 
                    if (row not in range(ROWS) or 
                    col not in range(COLS) or 
                    grid[row][col] != 1):
                        continue 
                    
                    # update cell 
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1 
            time += 1 
        
        return time if fresh == 0 else -1
