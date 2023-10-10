class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = 0
        currMin = 0
        globalMax = nums[0]
        globalMin = nums[0]
        totalSum = 0

        for n in nums:
            currMax = max(currMax + n, n)
            currMin = min(currMin + n, n)
            globalMax = max(currMax, globalMax)
            globalMin = min(currMin, globalMin)
            totalSum += n
        
        # edge case for handling array with negative input 
        if globalMax > 0:
            return max(totalSum - globalMin, globalMax)
        return globalMax
        