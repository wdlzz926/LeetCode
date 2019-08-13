class Solution(object):
    def edge_index(self, nums,target,left):
        lo = 0
        hi =len(nums)
        while lo<hi:
            mid = (lo+hi) //2
            if nums[mid]>target or (left and nums[mid] == target):
                hi = mid
            else:
                lo = mid+1
        return lo
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_idx = self.edge_index(nums,target,True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1,-1]
        return [left_idx, self.edge_index(nums,target,False)-1]
        
        