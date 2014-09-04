__author__ = 'samsung'

#

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        n = 9
        #row
        print 'row'
        for i in range(n):
            visited = []
            for j in range(n):
                if self.process(board[i][j], visited):
                    if board[i][j] != '.':visited.append(board[i][j])
                else:
                    return False
        #col
        print 'col'
        for i in range(n):
            visited = []
            for j in range(n):
                if self.process(board[j][i], visited):
                    if board[j][i] != '.':visited.append(board[j][i])
                else:
                    return False
        #3x3
        print '3x3'
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                visited = []
                for k in range(9):
                    if self.process(board[i+k/3][j+k % 3], visited):
                        if board[i+k/3][j+k % 3] != '.':visited.append(board[i + k / 3][j + k % 3])
                    else:
                        return False
        return True

    def process(self, cur, visited):
        if cur == '.':
            return True
        elif cur in visited:
            return False
        else:
            return True


s = Solution()
print s.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])