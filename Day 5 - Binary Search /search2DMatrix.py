# runtime 
# O(log m * n) = O(log m) + O(log n) by properties of logs 
# search for row = O(log m) where m represents the number of rows 
# search for target in row = O(log n) where n represents the number of cols 

# space - constant since no additional memory needed 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        # binary search the matrix to find the correct row 
        top = 0 
        bot = ROWS - 1
        while top <= bot:
            midRow = (top + bot) // 2 
            # look at the first element 
            if target > matrix[midRow][-1]:
                top = midRow + 1 
            elif target < matrix[midRow][0]:
                bot = midRow - 1 
            else:
                break 
        
        if not top <= bot:
            return False 
        
        midRow = (top + bot) // 2 
        # find the element in the row 
        lo = 0
        hi = COLS - 1 
        while lo <= hi:
            mid = (lo + hi) // 2 
            if matrix[midRow][mid] == target:
                return True 
            elif matrix[midRow][mid] < target:
                lo = mid + 1 
            else:
                hi = mid - 1 
        
        return False 
        