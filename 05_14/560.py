class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = cur = 0
        sum_map = {}
        sum_map[0] = 1
        for i in nums:
            cur += i
            if cur-k in sum_map:
                count += sum_map[cur-k]
            if cur in sum_map:
                sum_map[cur] += 1
            else:
                sum_map[cur] =1
            #sum_map[cur] = 1 if cur not in sum_map else sum_map[cur]+1
        return count