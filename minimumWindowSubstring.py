class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case 
        if t == "":
            return ""
        countT = {}
    
        # keep track of current window 
        window  = {}

        # count character frequency
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        L = 0

        for R in range(len(s)):
            c = s[R]
            window[c] = 1 + window.get(c, 0)

            # window == countT
            if c in countT and window[c] == countT[c]:
                have += 1 
            
            # check if have == need condition
            while have == need:
                # update result 
                if (R - L + 1) < resLen:
                    res = [L, R]
                    resLen = (R - L + 1)
                # minimize the window 
                # pop from the left of our window 
                window[s[L]] -= 1 
                if s[L] in countT and window[s[L]] < countT[s[L]]:
                    have -= 1
                L += 1 
        
        L, R = res 
        if resLen != float("infinity"):
            return s[L: R + 1]
        else:
            return ""


        