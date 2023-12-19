class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        - k -> represents the number of elements in nums which are not equal to val 
        - remove all ocurrences of val in nums in place 
        - the order of elements may be changed
        - runtime - O(n) where n represents the number of elements in nums
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