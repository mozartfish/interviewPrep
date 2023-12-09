class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        - Open: add open parenthesis if open < n
        - Close: add closing parenthsis if closed < open 
        - result iff open == closed == n
        '''

        stack = []
        result = []
        def backtrack(openN, closedN):
            # base case 
            if openN == closedN == n:
                result.append("".join(stack))
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop() 
        
        # call function with 0 because stack and result are empty initially
        backtrack(0, 0)
        return result