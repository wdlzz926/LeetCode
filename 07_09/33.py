class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)
        while left <right:
            mid = (left+right)//2
            cur_num = nums[mid]
            if target == cur_num:
                return mid
            elif cur_num <= nums[right-1] and nums[right-1] < nums[0]: # mid in second part
                if target >= nums[0]:
                    right = mid #target in first part
                elif target < cur_num:
                    right = mid
                elif target > cur_num:
                    left = mid+1
            else: # mid in first part 
                if target  < nums[0]:
                    left = mid+1
                elif target < cur_num:
                    right = mid
                elif target >cur_num:
                    left = mid+1
        return -1
                