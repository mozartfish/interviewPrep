# runtime - O(log n)
# space - O(n) additional space since we are dividing the search space on each recursive call 
class Solution:
    def binarySearch(self, arr, target, lo, hi):
        if lo > hi:
            return -1 
        
        mid = (lo + hi) // 2 
        if arr[mid] == target:
            return mid 
        elif arr[mid] > target:
            return self.binarySearch(arr, target, lo, mid - 1)
        else:
            return self.binarySearch(arr, target, mid + 1, hi)
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums) - 1)