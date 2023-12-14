class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''
        - n -> represents the length of nums array 
        - return array ans of length 2n where ans[i] and ans[i + n] == nums[i] for 0 <= i < n
        - ans is the concatenation of two nums arrays 
        '''
        n = len(nums)
        ans = [0 for i in range(2 * n)]

        for i, v in enumerate(nums):
            ans[i] = v
            ans[i + n] = v
        
        return ans 
        