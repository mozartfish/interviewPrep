class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        - nums array is sorted in non-decreasing order 
        - remove some duplicates in place such that each unique element appears at most twice 
        - relative order should be kept the same 
        '''

        L = 0 
        R = 0 
        while R < len(nums):
            count = 1 
            while R + 1 < len(nums) and nums[R] == nums[R + 1]:
                R += 1 
                count += 1 
            
            # update the values at L and R so that there are exactly two values
            for i in range(min(2, count)):
                nums[L] = nums[R]
                L += 1 
            R += 1 
        return L 