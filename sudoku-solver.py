  import math
  class Solution:
      def solveSudoku(self, board) -> None:

          n = len(board)
          self.backtrack(board,0, 0, n)
          print(board)
      def backtrack(self,board,row, col, n):
          if col == n:
              row = row+1
              col = 0
          if row == n:
              return True

          if(board[row][col] != "."):
              res = self.backtrack(board, row, col+1 ,n)
              if(res):return True

          else:
              for i in range(1,10):            
                  if(self.isSafe(row,col,str(i), board)):

                      board[row][col]=str(i)

                      res = self.backtrack(board,row,col+1,n)
                      if(res): return True

                      board[row][col]="."

          return False

      def isSafe(self, row, col, val, board):
          n = len(board)

          for r in range(n):
              if board[row][r] == val:
                  return False
              elif board[r][col] == val:
                  return False

          if(self.isInGrid(row,col,val, board)):
              return False
          return True

      def isInGrid(self, row, col, val, board):
            rowStart = math.floor(row/3)*3
            colStart = math.floor(col/3)*3

            for i in range(rowStart, rowStart+3):
                  for j in range(colStart, colStart+3):
                      if board[i][j] == val:
                          return True

            return False

  obj = Solution()

  obj.solveSudoku( [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
