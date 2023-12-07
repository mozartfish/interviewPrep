class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      '''
      - Rows, cols, boxes have to have unique values between 1-9
      Ideas
      - use sets to keep track of unique values
      '''
      from collections import defaultdict
      ROWS = defaultdict(set)
      COLS = defaultdict(set)
      box = defaultdict(set) # key = (r/3, c/3)
      for r in range(9):
        for c in range(9):
          if board[r][c] == ".":
            continue
          if (board[r][c] in ROWS[r] or
          board[r][c] in COLS[c] or
          board[r][c] in box[(r//3, c//3)]):
            return False 
          ROWS[r].add(board[r][c])
          COLS[c].add(board[r][c])
          box[(r//3, c//3)].add(board[r][c])
      return True 