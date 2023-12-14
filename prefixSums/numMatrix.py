class NumMatrix:
    '''
    - calculate the sum of the elements the elements of a rectangle within the matrix defined by upper left corner and lower right corner (row1, col1) and (row2, col2)
    - sumRegion must have a complexity of O(1)
    '''

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMatrix = [[0] * (COLS + 1) for R in range(ROWS + 1)]
        for r in range(ROWS):
            pSum = 0 
            for c in range(COLS):
                pSum += matrix[r][c]
                above = self.sumMatrix[r][c + 1]
                self.sumMatrix[r + 1][c + 1] = pSum + above
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # need to add one to query in to the main matrix
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.sumMatrix[row2][col2]
        above = self.sumMatrix[row1 - 1][col2]
        left = self.sumMatrix[row2][col1 - 1]
        topLeft = self.sumMatrix[row1 - 1][col1 - 1]
        return bottomRight - above - left + topLeft 
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)