class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        for num in nums:
            # current sum has to always be greater than 0
            currSum = max(currSum + num, num)
            # update maxSum 
            maxSum = max(maxSum, currSum)
        return maxSum 