class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # store unique values to keep track of duplicates
        numSet = set() 
        for num in nums:
            if num in numSet:
                return True 
            else:
                numSet.add(num)
        
        return False 