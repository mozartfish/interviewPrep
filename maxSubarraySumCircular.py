class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMaxSum = nums[0]
        globalMinSum = nums[0]
        currMaxSum = 0 
        currMinSum = 0
        totalSum = 0

        for n in nums:
            currMaxSum = max(n, currMaxSum + n)
            currMinSum = min(n, currMinSum + n)
            globalMaxSum = max(currMaxSum, globalMaxSum)
            globalMinSum = min(currMinSum, globalMinSum)
            totalSum += n

        if globalMaxSum > 0:
            return max(globalMaxSum, totalSum - globalMinSum)
        else:
            return globalMaxSum
        