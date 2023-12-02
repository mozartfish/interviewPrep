class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set() 
        for num in nums: 
            if num in numSet:
                return True 
            numSet.add(num)
        
        return False 
        
        