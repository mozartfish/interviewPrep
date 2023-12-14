class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        '''
        - variation of Kadane's Algorithm for Maximum Subarray
        '''
        currMax = 0
        currMin = 0
        globalMax = nums[0]
        globalMin = nums[0]
        totalSum = 0

        for num in nums:
            currMax = max(currMax + num, num)
            currMin = min(currMin + num, num)
            globalMax = max(currMax, globalMax)
            globalMin = min(currMin, globalMin)
            totalSum += num 
        
        # edge case for handling array with all negative values 
        if globalMax > 0:
            return max(totalSum - globalMin, globalMax)
        
        return globalMax 