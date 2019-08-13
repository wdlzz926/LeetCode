class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cursor = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[cursor] = nums[i]
                cursor += 1
        return cursor
        