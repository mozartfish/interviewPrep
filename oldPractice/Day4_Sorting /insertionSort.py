class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        for i in range(1, n):
            j = i - 1 # previous element 
            while j >= 0 and nums[j] > nums[j + 1]:
                temp = nums[j + 1]
                nums[j + 1] = nums[j]
                nums[j] = temp
                j -= 1
        
        return nums