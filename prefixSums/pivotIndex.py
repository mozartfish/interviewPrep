class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        - pivot index = index where the sum of all numbers strictly to the left of the index === sum of all numbers strictly to the index right 
        - if index on the left edge, left sum is 0 since there are so values to the left
        - return the leftmost pivot index. if no such index exists return -1
        '''

        # sum all the values 
        total = sum(nums) # this is O(n)
        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum 
            if leftSum == rightSum:
                return i 
            leftSum += nums[i]
        
        return -1