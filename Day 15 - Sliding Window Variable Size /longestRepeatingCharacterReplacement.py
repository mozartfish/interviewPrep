class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {} 
        length = 0 
        L = 0 
        # keep track of max frequent element 
        maxFr = 0 

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            maxFr = max(maxFr, count[s[R]])
            while R - L + 1 - maxFr > k:
                count[s[L]] -= 1
                L += 1 
            length = max(length, R - L + 1)

        return length 
