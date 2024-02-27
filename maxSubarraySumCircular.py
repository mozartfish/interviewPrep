class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMaxSum = nums[0]
        globalMinSum = nums[0]
        currMaxSum = 0
        currMinSum = 0
        totalSum = 0

        for n in nums:
            currMaxSum = max(currMaxSum + n, n)
            currMinSum = min(currMinSum + n, n)
            globalMaxSum = max(globalMaxSum, currMaxSum)
            globalMinSum = min(globalMinSum, currMinSum)
            totalSum += n 
            
        if globalMaxSum > 0:
            return max(totalSum - globalMinSum, globalMaxSum)
        else:
            return globalMaxSum
