class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # check for duplicates 
        # duplicate: return true 
        # else: return false 

        numSet = set() 

        for num in nums:
            if num in numSet:
                return True 
            else:
                numSet.add(num)
        
        return False 
        