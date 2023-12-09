class Solution:
    '''
    - need to match all parentheses (opening and closing)
    - runtime is O(n) since we have to go through all the elements in the string
    '''
    def isValid(self, s: str) -> bool:
        stack = []
        pMap = {"}": "{", "]": "[", ")": "("}
        
        for c in s:
            if c not in pMap:
                stack.append(c)
            elif not stack or stack[-1] != pMap[c]:
                return False
            else:
                stack.pop()

        return not stack 