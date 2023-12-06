class Solution:
    def merge(self, arr, start, mid, end):
        # create two arrays representing left and right halves
        left = arr[start:mid + 1]
        right = arr[mid + 1:end + 1]

        # variables for keeping track of indexes 
        i = 0
        j = 0
        k = start 

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
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
        
        return arr

    def mergeSort(self, arr, start, end):
        # check if we have an array of at least length 1 
        if end - start + 1 <= 1:
            return arr

        # calculate midpoint 
        mid = (start + end) // 2 
        
        # sort left half 
        self.mergeSort(arr, start, mid)

        # sort right half 
        self.mergeSort(arr, mid + 1, end)

        # merge sorted halves 
        self.merge(arr, start, mid, end)
        
        return arr 

    def sortArray(self, nums: List[int]) -> List[int]: 
        return self.mergeSort(nums, 0, len(nums) - 1)
        
