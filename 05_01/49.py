class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        keys = {}
        res = []
        count = 0
        for word in strs:
            temp = "".join(sorted(word))
            if temp not in keys:
                keys[temp] = count
                count += 1
                res.append([word])
            else:
                res[keys[temp]].append(word)
        return res
            