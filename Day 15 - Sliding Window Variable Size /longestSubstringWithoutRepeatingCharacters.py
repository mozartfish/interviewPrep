class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set the left pointer 
        L = 0
        # keep track of max length 
        length = 0 
        # keep track of duplicates 
        charSet = set() 

        for R in range(len(s)):
            while s[R] in charSet:
                charSet.remove(s[L])
                L += 1 
            charSet.add(s[R])
            length = max(length, R - L + 1)
        
        return length


