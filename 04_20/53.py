#DP solution

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        curSum = maxSum = nums[0]
        for i in range(1,len(nums)):
            curSum = max(curSum+nums[i], nums[i])
            maxSum = max(maxSum, curSum)
        return maxSum

#genuis version:
for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums)

#D&C: Time exceed
class Solution(object):
    
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        return maxSub(nums, 0, len(nums)-1)
    
def maxSub(nums, l, r):
    if l==r:
        return nums[l]
    mid = int((l+r)/2)
    l_max = maxSub(nums,l,mid)
    r_max = maxSub(nums,mid+1,r)
    r_s = nums[mid+1]
    l_s = nums[mid]
    s = 0
    for i in list(reversed(nums[l:mid+1])):
        s += i
        l_s = max(l_s, s)
    s=0
    for i in nums[mid+1:]:
        s += i
        r_s = max(r_s, s)
    max_mid = l_s+r_s
    max_two = max(l_max, r_max)
    return max(max_two,max_mid)