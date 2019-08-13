class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        counter = set()
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] != '.':
                    cur = board[i][j]
                    if (i, cur) in counter or (cur,j) in counter or (i/3,j/3,cur) in counter:
                        return False
                    counter.add((i,cur))
                    counter.add((cur,j))
                    counter.add((i/3,j/3,cur))
        return True