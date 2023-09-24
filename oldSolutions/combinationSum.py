# runtime - 0(2^n)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subset = []
        result = []
        totalSum = 0

        def dfs(i, subset, totalSum):
            if totalSum == target:
                result.append(subset.copy())
                return 
            if i > len(candidates) - 1 or totalSum > target:
                return 
            subset.append(candidates[i])
            dfs(i, subset, totalSum + candidates[i])
            subset.pop() 
            dfs(i + 1, subset, totalSum)
        
        dfs(0, subset, totalSum)
        return result