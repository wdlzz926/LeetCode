class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = dict()
        for i in range(len(nums)):
            if nums[i] in dic:
                return True
            else:
                dic[nums[i]] = i
        return False