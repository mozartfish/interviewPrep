# runtime - 0(n) where n represents the number of elements 
# space = constants since no additional space is allocated
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1 
        k = 1 
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                i += 1 
            else:
                nums[k] = nums[i]
                i += 1 
                k += 1 
        
        return k 

