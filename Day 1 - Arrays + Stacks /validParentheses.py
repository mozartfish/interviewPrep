# runtime - O(n) where n represents the length of the string 
# space - constant since no additional space allocated per element 
class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        parens = {")":"(", "]":"[", "}": "{"}
        for ch in s:
            if ch not in parens:
                stack.append(ch)
            elif not stack or parens[ch] != stack[-1]:
                return False 
            else:
                stack.pop() 
        return not stack 
        