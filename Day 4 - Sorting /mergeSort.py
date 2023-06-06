#  - O(n log n)
# - requires extra memory 
# - stable sort 

class Solution:
    def merge(self, arr, start, mid, end):
        left = arr[start:mid + 1]
        right = arr[mid + 1:end + 1]
        i = 0
        j = 0
        k = start 
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1 
            else:
                arr[k] = right[j]
                j += 1
            k += 1 
        while i < len(left):
            arr[k] = left[i]
            i += 1 
            k += 1 
        while j < len(right):
            arr[k] = right[j]
            j += 1 
            k += 1 
        return

    def mergeSort(self, arr, start, end):
        if end - start + 1 <= 1:
            return arr 
        
        mid = (start + end) // 2 
        self.mergeSort(arr, start, mid)
        self.mergeSort(arr, mid + 1, end)
        self.merge(arr, start, mid, end)
        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums))

