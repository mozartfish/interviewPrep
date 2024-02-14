class Solution:
    '''
    - integer array nums with length n 
    - return an integer array ans with length 2 * n where ans[i] == nums[i] and ans[i + n] == nums[i]
    '''
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0 for i in range(2 * n)]
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans 
        