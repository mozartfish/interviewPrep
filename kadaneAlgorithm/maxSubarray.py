class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        - find the subarray with the largest sum and return just the sum 
        - to maximize sum we always want to add positive values 
        - use kadane's algorithm
        '''
        currSum = 0
        maxSum = nums[0]
        for num in nums:
            currSum = max(currSum + num, num)
            maxSum = max(maxSum, currSum)
        return maxSum
        