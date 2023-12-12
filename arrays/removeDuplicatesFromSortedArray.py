class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        - remove all occurences of number val in array nums in place -> no extra memory 
        - order of elements may be changed 
        - return the number of elements which are not equal to val 
        - k represents the number of elements which are not equal to val 
        '''
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