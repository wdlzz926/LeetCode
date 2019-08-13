class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = list()
        key = {"}":"{", "]": "[",")": "("}
        if not s:
            return True
        a.append(s[0])
        for p in s[1:]:
            if p in key:
                if len(a) ==0:
                    return False
                top = a.pop()
                if top != key[p]:
                    return False
            else:
                a.append(p)
        return not a