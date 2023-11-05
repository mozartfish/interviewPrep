class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # - length of strings have to match 
        # - char counts have to match to be a palindrome 

        if len(s) != len(t):
            return False 
        
        charMap = {} 
        for c in s:
            if c not in charMap:
                charMap[c] = 1 
            else:
                charMap[c] += 1 
        
        for c in t:
            if c not in charMap:
                return False 
            if c in charMap:
                charMap[c] -= 1 
            if charMap[c] == 0:
                del charMap[c]
        return not charMap