class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
         - algorithm has to have a run time of O(n)
         - cannot use the divison operator 
        '''
        
        result = [0 for i in range(len(nums))]

        # prefix 
        prefix = 1 
        for i in range(len(nums)):
            result[i] = prefix 
            prefix *= nums[i]
        
        # postfix 
        postfix = 1 
        for j in range(len(nums) - 1, - 1, -1):
            result[j] *= postfix 
            postfix *= nums[j]
        
        return result 
        