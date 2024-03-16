# Valid Palindrome 
class Solution:
    def isAlphaNum(self, ch):
        if ord('a') <= ord(ch) <= ord('z'):
            return True 
        elif ord('0') <= ord(ch) <= ord('9'):
            return True 
        else:
            return False 

    def isPalindrome(self, s: str) -> bool:
        # convert string to lower case 
        s = s.lower() 
        L = 0
        R = len(s) - 1 

        while L < R:
            while not self.isAlphaNum(s[L]) and L < R:
                L += 1 
            while not self.isAlphaNum(s[R]) and L < R:
                R -= 1 
            if s[L] != s[R]:
                return False 
            L += 1 
            R -= 1 
        return True
        