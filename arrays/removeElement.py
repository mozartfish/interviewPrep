class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        - elements are sorted in non-decreasing order -> monotonically increasing 
        - remove elements in place -> no additional memory 
        - relative order of numbers should be kept same -> same index 
        - return the number of unique elements which are represented by variable k 
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
        