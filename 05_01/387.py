class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        keys = {}
        for letter in s:
            if letter in keys:
                keys[letter] += 1
            else:
                keys[letter] =1
        for i in range(len(s)):
            if keys[s[i]] == 1:
                return i
        return -1