class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        - runtime has to be O(log(m * n))
        - this can be simplified as O(log m) + O(log n) by log properties 
        - which indicates we need to do 2 binary searches 
        '''
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # binary search matrix 
        top = 0 
        bot = ROWS - 1 

        while top <= bot:
            midRow = (top + bot) // 2 
            if target > matrix[midRow][-1]:
                top = midRow + 1 
            elif target < matrix[midRow][0]:
                bot = midRow - 1
            else:
                # found the row or exhausted all possible solutions 
                break 
        
        # check to see if we found a row 
        if not top <= bot:
            return False 
        
        # binary search row to find value 
        midRow = (top + bot) // 2 
        lo = 0
        hi = COLS - 1
        while lo <= hi:
            mid = (lo + hi) // 2 
            if matrix[midRow][mid] == target:
                return True 
            elif matrix[midRow][mid] > target:
                hi = mid - 1 
            else:
                lo = mid + 1 
        
        return False 