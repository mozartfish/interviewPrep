class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        charSet = set() 
        L = 0
        for R in range(len(s)):
            while s[R] in charSet:
                charSet.remove(s[L])
                L += 1 
            charSet.add(s[R])
            length = max(R - L + 1, length)
        return length 
        