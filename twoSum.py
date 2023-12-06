class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      '''
      - exactly one unique solution 
      - cannot use the same element twice - has to be different indices
      Ideas
      1. map each number in list to its index and return index 
      ''' 
      numMap = {}
      for indx, num in enumerate(nums):
        diff = target - num
        if diff in numMap:
          return [numMap[diff], indx]
        else:
          numMap[num] = indx 
      return []
        