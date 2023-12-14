class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() 
        result = 0
        L = 0 
        for R in range(len(s)):
            while s[R] in charSet:
                charSet.remove(s[L])
                L += 1 
            charSet.add(s[R])
            result = max(result, R - L + 1)
        return result 
        