class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float('inf')
        L, total = 0, 0
        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                length = min(R - L + 1, length)
                total -= nums[L]
                L += 1 
        if length == float('inf'):
            return 0 
        else:
            return length 
        