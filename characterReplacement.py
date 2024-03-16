class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        L = 0
        maxF = 0 
        length = 0 
        
        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            while (R - L + 1) - maxF > k:
                count[s[L]] -= 1 
                L += 1 
            length = max(R - L + 1, length)
        return length
        