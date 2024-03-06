class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} 
        maxF = 0 
        L = 0 
        length = 0 
        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            maxF = max(maxF, count[s[R]])
            while (R - L + 1) - maxF > k:
                count[s[L]] -= 1 
                L += 1 
            length = max(R - L + 1, length)
            
        return length 
        