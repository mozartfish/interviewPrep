class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # set left pointer
        L = 0
        # keep track of rolling sum 
        totalSum = 0
        # length tracker 
        length = float("inf")
        
        for R in range(len(nums)):
            totalSum += nums[R]
            while totalSum >= target:
                length = min(R - L + 1, length)
                totalSum -= nums[L]
                L += 1 
        
        if length == float("inf"):
            return 0
        else:
            return int(length)

