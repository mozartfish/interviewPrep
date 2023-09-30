class Solution:
    def partition(self, arr, start, end):
        pivot = arr[end]
        i = start
        for j in range(start, end):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1 
        arr[i], arr[end] = arr[end], arr[i]
        return i
        
    def quickSelect(self, arr, start, end, k):
        pivotIndex = self.partition(arr, start, end)
        if k < pivotIndex:
            return self.quickSelect(arr, start, pivotIndex - 1, k)
        elif k > pivotIndex:
            return self.quickSelect(arr, pivotIndex + 1, end, k)
        return arr[pivotIndex]
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # find kth element using 0 based counting
        k = len(nums) - k 
        return self.quickSelect(nums, 0, len(nums) - 1, k)
        