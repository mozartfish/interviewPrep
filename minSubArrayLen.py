class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0 
        length = float("infinity")
        totalSum = 0 
        for R in range(len(nums)):
            totalSum += nums[R]
            while totalSum >= target:
                length = min(length, R - L + 1)
                totalSum -= nums[L]
                L += 1 
                
        return 0 if length == float("infinity") else length