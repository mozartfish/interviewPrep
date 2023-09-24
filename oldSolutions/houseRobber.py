class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge cases
        if len(nums) == 0 or None:
            return 0 
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        cache = {} 
        cache[0] = nums[0]
        cache[1] = max(nums[0], nums[1])
        n = len(nums)

        for i in range(2, n):
            cache[i] = max(nums[i] + cache[i - 2], cache[i - 1])
        
        return cache[n - 1]