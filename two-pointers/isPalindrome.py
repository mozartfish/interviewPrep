class Solution:
    def alphaNum(self, ch): 
        # check whether character is an alphanumeric using ascii 
        return (ord('a') <= ord(ch) <= ord('z') or ord('0') <= ord(ch) <= ord('9'))
    def isPalindrome(self, s: str) -> bool:
        '''
        - palindrome -> a string that reads the same forwards and backwards 
        - string contains all alphanumeric characters -> a-z, A-Z, 0-9
        - need to check for all alphanumeric characters
        - string can contain mixed case and spaces -> need to make string uniform and skip spaces 
        - can be given empty string 
        '''
        # standardize string 
        s = s.lower() 
        L = 0
        R = len(s) - 1 

        while L < R:
            # skip non ascii characters 
            while L < R and not self.alphaNum(s[L]):
                L += 1 
            while L < R and not self.alphaNum(s[R]):
                R -= 1 
            # check for same character 
            if s[L] != s[R]:
                return False 
            L += 1 
            R-= 1 
        
        return True 





        