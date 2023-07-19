

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMin, globalMax = nums[0], nums[0]
        currMin, currMax = 0, 0 
        totalSum = 0

        for num in nums:
            currMax = max(currMax + num, num)
            currMin = min(currMin + num, num)
            totalSum += num
            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)
        
        if globalMax > 0:
            return max(globalMax, totalSum - globalMin)
        else:
            return globalMax
        
