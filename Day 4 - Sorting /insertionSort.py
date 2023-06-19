# runtime - 0(n^2)
# space - constant so no additional memory needed 
# stable sorting algorithm
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            j = i - 1 
            while j >=0 and nums[j + 1] < nums[j]:
                temp = nums[j + 1]
                nums[j + 1] = nums[j]
                nums[j] = temp 
                j -= 1 
        
        return nums
        