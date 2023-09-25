class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        k = 0
        while i < len(nums):
            if nums[i] == val:
                i += 1 
            else:
                nums[k] = nums[i]
                i += 1 
                k += 1 
        
        return k
        