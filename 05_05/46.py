#in place
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0: return []
        if len(nums) == 1: return [nums]
        res = []
        for i in range(len(nums)):
            for j in self.permute(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + j)
        return res

#backtrace
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            if first == len(nums):
                res.append(nums[:])
            for i in range(first,len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        res = []
        backtrack()
        return res