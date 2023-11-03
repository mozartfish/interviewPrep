class Solution:
    def alphaNum(self, char):
        return (ord("a") <= ord(char) <= ord("z") or 
        ord("A") <= ord(char) <= ord("Z") or 
        ord("0") <= ord(char) <= ord("9"))

    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1 
        s = s.lower() 

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
        