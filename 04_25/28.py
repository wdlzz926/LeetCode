class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_h = len(haystack)
        len_n = len(needle)
        if len_n == 0:
            return 0
        if  len_h < len_n:
            return -1
        for i in range(len_h-len_n+1):
            match = True
            for j in range(len_n):
                if haystack[i+j] != needle[j]:
                    match  = False
                    break
            if match:
                return i
        return -1