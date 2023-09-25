class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parens = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if ch not in parens:
                stack.append(ch)
            elif not stack or parens[ch] != stack[-1]:
                return False 
            else:
                stack.pop()
        return not stack