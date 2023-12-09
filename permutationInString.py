class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      '''
      - anagrams are permutations of a string 
      - check whether s2 contains an anagram of s1 
        Ideas 
        - use regex to find s1 in s2
      '''

      # edge case 
      if len(s1) > len(s2):
        return False 
      
      # create hashmaps 
      s1Count = [0] * 26
      s2Count = [0] * 26
      for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1 
        s2Count[ord(s2[i]) - ord('a')] += 1 
      
      matches = 0
      for i in range(26):
        if s1Count[i] == s2Count[i]:
          matches += 1 
        else:
          matches += 0
      
      # sliding window 
      L = 0 
      for R in range(len(s1), len(s2)):
        if matches == 26:
          return True 
        
        # right character
        index = ord(s2[R]) - ord('a')
        s2Count[index] += 1 
        if s1Count[index] == s2Count[index]:
          matches += 1 
        elif s1Count[index] + 1 == s2Count[index]:
          matches -= 1 
        
        # left character
        index = ord(s2[L]) - ord('a')
        s2Count[index] -= 1 
        if s1Count[index] == s2Count[index]:
          matches += 1 
        elif s1Count[index] - 1 == s2Count[index]:
          matches -= 1 
        
        # update pointer 
        L += 1 
      
      return matches == 26