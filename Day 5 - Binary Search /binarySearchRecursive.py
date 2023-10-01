class Solution:
    def binarySearch(self, arr, target, lo, hi):
        # base case 
        if lo > hi:
            return -1
        
        # calculate mid value
        mid = (lo + hi) // 2 
        
        if arr[mid] == target:
            return mid 
        elif arr[mid] > target:
            return self.binarySearch(arr, target, lo, mid - 1)
        else:
            return self.binarySearch(arr, target, mid + 1, hi)
        
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums) - 1)