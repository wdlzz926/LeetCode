#Vertical scanning
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs:
                if len(s)==i or s[i] != c:
                    return strs[0][0:i]
        return strs[0]   
            
        