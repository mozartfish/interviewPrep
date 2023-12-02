class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagrams have the same lengths and characters 
        if len(s) != len(t):
            return False 
        
        sMap = {} 
        for ch in s:
            if ch not in sMap:
                sMap[ch] = 1 
            else:
                sMap[ch] += 1 
        
        for ch in t:
            if ch not in sMap:
                return False 
            if ch in sMap:
                sMap[ch] -= 1 
            if sMap[ch] == 0:
                del sMap[ch]
        
        return not sMap
        