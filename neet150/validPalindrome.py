class Solution:
    def alphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        # standardize string - lowercase all chars 
        # check if characters is a number or letter 
        # skip non alphanumeric characteracters 
        # two pointers
        s = s.lower() 
        L = 0
        R = len(s) - 1 
        
        while L < R:
            # skip all non alphanumeric characters
            while L < R and not self.alphaNum(s[L]):
                L += 1 
            while L < R and not self.alphaNum(s[R]):
                R -= 1 
            # check if characters match 
            if s[L] != s[R]:
                return False 
            L += 1 
            R -= 1 
        return True 
