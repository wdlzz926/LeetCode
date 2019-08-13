class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        answer = [0] * length
        answer[0] = 1
        for i in range(1,length):
            answer[i] = answer[i-1]*nums[i-1]
        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i]*R
            R *= nums[i]
        return answer
        