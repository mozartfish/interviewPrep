class Solution:
    def generateKey(self, s):
      charCount = [0 for i in range(26)]
      # map character count to character ascii values to create a unique key 
      for ch in s:
        indx = ord(ch) - ord('a')
        charCount[indx] += 1 
      return tuple(charCount)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      '''
      - All anagrams share the same letters 
      Ideas
      - map sorted letters in anagram to list of words with same letters - cost is O(n log n) for the sort 
      - count unique character frequencies and use that as a key 
      '''
      anagramMap = {} 
      for s in strs:
        key = self.generateKey(s)
        if key not in anagramMap:
          words = [s]
          anagramMap[key] = words 
        else:
          words = anagramMap[key]
          words.append(s)
          anagramMap[key] = words 
      
      values = anagramMap.values() 

      return list(values)
