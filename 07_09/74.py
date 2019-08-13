class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        total = m*n
        left = 0
        right = total
        while left < right:
            mid = (left+right) //2
            fd = mid // n
            sd = mid % n
            cur_num = matrix[fd][sd]
            if target == cur_num:
                return True
            elif target < cur_num:
                right = mid
            else:
                left = mid+1
        return False