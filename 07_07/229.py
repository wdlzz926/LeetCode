class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        candidate1, count1, candidate2, count2 = 0,0,1,0
        for n in nums:
            if n == candidate1:
                count1+=1
            elif n == candidate2:
                count2+=1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 ==0:
                candidate2, count2 = n,1
            else:
                count1-=1
                count2-=1
        return [n for n in(candidate1, candidate2) if nums.count(n)>len(nums)//3]