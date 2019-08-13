class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        result = []
        for word in words[::-1]:
            result.append(word)
        return " ".join(result)