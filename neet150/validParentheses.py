class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pMap = {"}": "{", ")": "(", "]": "["}

        for c in s:
            if c not in pMap:
                stack.append(c)
            elif not stack or stack[-1]!= pMap[c]:
                return False 
            else:
                stack.pop()
            
        return not stack 