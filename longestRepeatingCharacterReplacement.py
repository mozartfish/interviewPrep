class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      '''
      - count the character frequencies 
      - choose a character and replace it up to k times 
      - substring -> continguous array of characters
      - shift pointer to keep string valid 
      - return the length of the longest subtring containing the same letter you can get after performing operations in the problem 
      '''   

      count = {}
      result = 0
      L = 0
      maxF = 0
      for R in range(len(s)):
        count[s[R]] = 1 + count.get(s[R], 0)
        maxF = max(maxF, count[s[R]])
        # move pointers to have a valid window range that satisfies k replacements
        # while (R - L + 1) - max(count.values()) > k:
        while (R - L + 1) - maxF > k:
          count[s[L]] -= 1 
          L += 1 
        result = max(result, R - L + 1)
      return result 