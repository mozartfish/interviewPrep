# O(nlogn) in the best case - worst case O(n^2) depending on the pivot, how sorted the array is 
# in place sort 
# unstable 
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(nums, start, end):
            if end - start + 1 <= 1:
                return 
            pivot = nums[end]
            left = start
            # partition 
            for i in range(start, end):
                if nums[i] < pivot:
                    temp = nums[left]
                    nums[left] = nums[i]
                    nums[i] = temp
                    left += 1 
            nums[end] = nums[left]
            nums[left] = pivot
            # sort everything left to pivot 
            quickSort(nums, start, left - 1)
            # sort everything to right of pivot 
            quickSort(nums, left + 1, end)
        
        quickSort(nums, 0, len(nums) - 1)
        return nums 