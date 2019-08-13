class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        candidates = sorted(candidates)
        
        def dfs(target, result,level):
            if target == 0:
                results.append(result)
                return
            for i in range(level, len(candidates)):
                if target - candidates[i] <0:
                    break
                else:
                    dfs(target-candidates[i],result+[candidates[i]], i)
        dfs(target, [], 0)
        return results                   