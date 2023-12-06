class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      '''
      - anagrams have same length 
      - anagrams have same characters 
      ''' 
      # check if t is an anagram of the characters in s 
      if len(s) != len(t):
        return False 
      
      # process s 
      sMap = {}
      for ch in s:
        sMap[ch] = 1 + sMap.get(ch, 0)
      
      # process t:
      for ch in t:

        # characters do not match 
        if ch not in sMap:
          return False 

        # characters match 
        if ch in sMap:
          sMap[ch] -= 1 
        
        # remove the character from map if its count is 0
        if sMap[ch] == 0:
          del sMap[ch]
      
      return not sMap


        