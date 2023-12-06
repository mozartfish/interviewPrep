class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # set up boiler plate info
        from collections import deque
        ROWS, COLS = len(grid), len(grid[0])
        visited = set() 
        q = deque() 

        # directions - 8 way directions 
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0], 
        [1,  1], [1, -1], [-1, 1], [-1, -1]]

        # boundary case 
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1 

        # bfs algorithm 
        q.append((0, 0, 1))
        visited.add((0 , 0))

        while len(q) > 0:
            for i in range(len(q)):
                r, c, dist = q.popleft() 
                # boundary cases 
                if r == ROWS - 1 and c == COLS - 1:
                    return dist 
                for dr, dc in dir:
                    row, col = r + dr, c + dc 
                    if (row in range(ROWS) and 
                    col in range(COLS) and 
                    grid[row][col] == 0 and
                    (row, col) not in visited):
                        q.append((row, col, 1 + dist))
                        visited.add((row, col))
        
        return -1
        