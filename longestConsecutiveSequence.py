class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      '''
      - algorithm has to run in O(n) time -> no sorting 
      - track the length of the longest CONSECUTIVE SEQUENCE
      Ideas 
      - need to keep track of the length of the longest -> use set  
      '''

      longest = 0
      numSet = set(nums)
      for num in nums:
        # check if we are starting a sequence 
        if (num - 1) not in numSet:
          # keep track of current sequence length
          length = 0
          # check if a conseuctive number is in the list of numbers
          while (num + length) in numSet:
            length += 1 
          # update sequence length
          longest = max(longest, length)
      return longest