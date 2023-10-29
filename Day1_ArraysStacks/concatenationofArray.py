class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0 for i in range(2 * n)]
        for indx, val in enumerate(nums):
            ans[indx] = val 
            ans[indx + n] = val 
        
        return ans
        