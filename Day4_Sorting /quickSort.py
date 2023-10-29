class Solution:
    def partition(self, arr, start, end):
        pivot = arr[end]
        i = start - 1
        for j in range(start, end):
            if arr[j] <= pivot:
                i += 1 
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[end] = arr[end], arr[i + 1]
        return i + 1

    def quickSort(self, arr, start, end):
        if start < end:
            pivotIndex = self.partition(arr, start, end)
            self.quickSort(arr, start, pivotIndex - 1)
            self.quickSort(arr, pivotIndex + 1, end)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums