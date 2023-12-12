class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''
        - ans array has length of 2 * n where n represents length of original array 
        - ans[i] == nums[i]
        - ans[i + n] == nums[i]
        '''
        n = len(nums)
        ans = [0 for i in range(2 * n)]
        for i, v in enumerate(nums):
            ans[i] = v 
            ans[i + n] = v 
        
        return ans