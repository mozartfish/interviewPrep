class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        - k -> total number of unique elements in nums 
        - nums is sorted in non-decreasing order
        - required to remove duplicates in place such that each unique element appears only once 
        - relative order of elements should be kept the same 
        '''

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
