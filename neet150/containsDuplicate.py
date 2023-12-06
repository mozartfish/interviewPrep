class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      '''
      - create a set 
      - look for duplicates and return true if any 
      '''

        numSet = set()

        for num in nums:
          if num in numSet:
            return True 
          else:
            numSet.add(num)
        
        return False 