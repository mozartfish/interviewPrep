class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # exact same length 
        # exact same character frequency 
        if len(s) != len(t):
            return False 
        charMap = {} 

        # string s 
        for ch in s:
            if ch not in charMap:
                charMap[ch] = 1 
            else:
                charMap[ch] += 1 
        
        # string t 
        for ch in t:
            if ch not in charMap:
                return False 
            if ch in charMap:
                charMap[ch] -= 1 
            if charMap[ch] == 0:
                del charMap[ch]
        
        return not charMap
        
        
