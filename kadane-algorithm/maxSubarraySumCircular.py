class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax = nums[0]
        globalMin = nums[0]
        currMax = 0
        currMin = 0
        totalSum = 0

        for num in nums:
            currMax = max(currMax + num, num)
            currMin = min(currMin + num, num)
            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)
            totalSum += num

        
        if globalMax > 0:
            return max(totalSum - globalMin, globalMax)
        
        # handle the case for all negative values
        return globalMax
        