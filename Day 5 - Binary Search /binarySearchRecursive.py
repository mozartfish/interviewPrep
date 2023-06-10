class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1 
        while lo <= hi:
            mid = (lo + hi) // 2 
            if nums[mid] < target:
                lo = mid + 1 
            elif nums[mid] > target:
                hi = mid - 1 
            else:
                return mid
        return -1