class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      '''
      - substring -> contiguous array of characters
      - find length of longest substring without repeating characters -> going to need a set to keep track of unique characters
      '''
      charSet = set() 
      result = 0
      L = 0
      for R in range(len(s)):
        # check substring for repeating characters
        while s[R] in charSet:
          charSet.remove(s[L])
          L += 1 
        # start a new substring 
        charSet.add(s[R])
        result = max(result, R - L + 1)
      return result 
        