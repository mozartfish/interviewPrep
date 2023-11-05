class Solution:
    def alphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or 
        ord('0') <= ord(c) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        # standardize characters - lowercase all chars 
        # check if character is a number and letter 
        # skip non alpha numeric characters
        # two pointers - 

        s = s.lower() 
        L = 0 
        R = len(s) - 1 

        while L < R:
            # skip all non alpha num 
            while L < R and not self.alphaNum(s[L]):
                L += 1 
            while L < R and not self.alphaNum(s[R]):
                R -= 1 
            # check for matching characters 
            if s[L] != s[R]:
                return False 
            
            L += 1 
            R -= 1 
        return True 