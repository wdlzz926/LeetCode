#Hash table
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            if i in hash_table:
                hash_table.pop(i)
            else:
                hash_table[i] = 1
        return hash_table.popitem()[0]

#Bit manipulation
class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a