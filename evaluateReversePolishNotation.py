class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        - use a stack to keep track of all the different tokens 
        - order matters for subtraction and divison 
        '''
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
                # pass 
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
                # pass 
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
                # pass 
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
                # pass 
            else:
                stack.append(int(c))
        
        return stack[0]