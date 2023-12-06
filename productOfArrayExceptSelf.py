class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        - cannot use the division operator 
        - runtime has to be O(n)
        '''

        result = [1 for i in range(len(nums))]

        # prefix 
        prefix = 1 
        for i in range(len(nums)):
          result[i] = prefix # result[i] = result[i] * prefix where result[i] is always 1 in this case 
          prefix = prefix * nums[i]
        
        # postfix 
        postfix = 1 
        for j in range(len(nums) - 1, -1, -1):
          result[j] = result[j] * postfix 
          postfix = postfix * nums[j]

        return result 
