# Concatentation of Array
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0 for j in range(2 *n)]

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        
        return ans
        