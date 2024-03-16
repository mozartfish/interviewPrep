# Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                i += 1 
            else:
                nums[k] = nums[i]
                i += 1
                k += 1 
        return k
        