class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" or s[0] == "0": 
            return 0
        dp1 = 1
        dp2 = 1
        for i in range(1, len(s)):
            if s[i] == "0" and (s[i - 1] == "0" or s[i - 1] >= "3"): 
                return 0
            if s[i] == "0":
                dp1, dp2 = dp2,dp1
            elif 10< int(s[i-1:i+1]) <= 26:
                dp1, dp2 = dp2, dp1+dp2
            else:
                dp1 = dp2
        return dp2
                