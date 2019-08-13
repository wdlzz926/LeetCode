class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        def search(i,j,level):
            if not (0 <= i and i < self.rows and 0 <= j and j < self.cols):
                return False
            if self.board[i][j] != word[level]:
                return False
            if level == self.wordLen-1:
                return True
            temp = self.board[i][j]
            self.board[i][j] = "#" #mark visited
            res = search(i,j+1,level+1) or search(i+1,j,level+1) or search(i-1,j,level+1) or search(i,j-1,level+1)
            self.board[i][j] = temp
            return res
        
        if len(board) == 0:
            return False
        self.rows = len(board)
        self.cols = len(board[0])
        self.wordLen = len(word)
        self.board = board
        self.word = word
        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(i,j,0):
                    return True
        return False
            
        