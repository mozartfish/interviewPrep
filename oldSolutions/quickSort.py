# runtime - O(n^2) worst case, O(nlogn) average/best case depending on pivot 
# space - constant and in place sort 
# stability - unstable 
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(nums, start, end):
            if end - start + 1 <= 1:
                return 
            pivot = nums[end]
            left = start 
            for i in range(start, end):
                if nums[i] < pivot:
                    temp = nums[left]
                    nums[left] = nums[i]
                    nums[i] = temp 
                    left += 1 
            nums[end] = nums[left]
            nums[left] = pivot 
            quickSort(nums, start, left - 1)
            quickSort(nums, left + 1, end)
        
        quickSort(nums, 0, len(nums) - 1)
        return nums
        