class Solution:
    def alphaNum(self, ch):
        return (ord('a') <= ord(ch) <= ord('z') or ord('0')  <= ord(ch) <= ord('9'))
        
    def isPalindrome(self, s: str) -> bool:
        # standardize string 
        s = s.lower() 
        L = 0
        R = len(s) - 1 

        while L < R:
            while L < R and not self.alphaNum(s[L]):
                L += 1 
            while L < R and not self.alphaNum(s[R]):
                R -= 1 
            if s[L] != s[R]:
                return False 
            L += 1 
            R -= 1 
        return True 

        