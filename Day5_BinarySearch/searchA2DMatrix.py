class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        # binary search matrix to find row 
        top = 0 # lo
        bot = ROWS - 1 # hi 
        while top <= bot:
            midRow = (top + bot) // 2 
            if target > matrix[midRow][-1]:
                top = midRow + 1 
            elif target < matrix[midRow][0]:
                bot = midRow - 1 
            else:
                # found row or exhausted all options 
                break
        
        if not top <= bot:
            return False 
        
        # get the row to find value 
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
        