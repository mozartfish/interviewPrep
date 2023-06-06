# runtime - O(n ^ 2) in the worst case 
# in place sort 
# stable sort 
# python sort -> TimSort = mergeSort + insertion sort to get O(nlogn) or O(n)
# depending on the number of elements and how sorted the array 
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(1, n):
            j = i - 1 
            while j >= 0 and nums[j + 1] < nums[j]:
                temp = nums[j + 1]
                nums[j + 1] = nums[j]
                nums[j] = temp 
                j -= 1 
        
        return nums

