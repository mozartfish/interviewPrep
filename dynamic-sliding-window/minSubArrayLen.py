class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float("infinity")
        L = 0
        totalSum = 0

        for R in range(len(nums)):
            totalSum += nums[R]
            while totalSum >= target:
                minLength = min(minLength, R - L + 1)
                totalSum -= nums[L]
                L += 1 
        
        if minLength == float("infinity"):
            return 0 
        else:
            return minLength