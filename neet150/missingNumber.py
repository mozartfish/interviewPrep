class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        n = len(nums)

        for i in range(n):
            result += i - nums[i]
        
        return result