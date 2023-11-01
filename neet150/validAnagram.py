class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # original letters need to be used exactly once - same length
        if len(s) != len(t):
            return False 
        
        # character frequency has to match - count characters with a map 
        sCount = {}
        for c in s:
            if c not in sCount:
                sCount[c] = 1 
            else:
                sCount[c] += 1 
        
        for c in t:
            if c not in sCount:
                return False 

            if c in sCount:
                sCount[c] -= 1

            if sCount[c] == 0:
                del sCount[c]
        
        return not sCount
        