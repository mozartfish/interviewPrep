class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        total = 0
        length = float('inf')

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                length = min(length, R - L + 1)
                total -= nums[L]
                L += 1
                
        if length == float('inf'):
            return 0 
        else:
            return length 