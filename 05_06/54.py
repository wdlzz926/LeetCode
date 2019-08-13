class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def oneLevel(r1,c1,r2,c2):
            for c in range(c1,c2+1):
                yield r1,c
            for r in range(r1+1,r2+1):
                yield r,c2
            if r1 < r2 and c1 <c2:
                for c in range(c2-1, c1,-1):
                    yield r2,c
                for r in range(r2, r1,-1):
                    yield r,c1
        if not matrix:
            return []
        res = []
        r1, r2 = 0, len(matrix)-1
        c1, c2 = 0, len(matrix[0])-1
        while r1 <= r2 and c1 <= c2:
            for r,c in oneLevel(r1,c1,r2,c2):
                res.append(matrix[r][c])
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        return res