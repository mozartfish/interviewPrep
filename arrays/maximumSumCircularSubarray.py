class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = 0
        currMin = 0 
        globalMax = nums[0]
        globalMin = nums[0]
        totalSum = 0

        for num in nums:
            currMax = max(currMax + num, num)
            currMin = min(currMin + num, num)
            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)
            totalSum += num
        
        # handle at least one positive 
        if globalMax  > 0:
            return max(totalSum - globalMin, globalMax)
        
        # handle negative maxmium sum - every value is negative
        return globalMax 

