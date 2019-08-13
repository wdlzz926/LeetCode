class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def recur(S, left, right):
            if (len(S) == 2*n):
                res.append(S)
                return
            if left<n:
                recur(S+'(', left+1, right)
            if right<left:
                recur(S+')',left, right+1)
        
        recur("", 0,0)
        return res