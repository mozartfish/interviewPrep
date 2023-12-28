class MinStack:
    '''
    - all operations have to be O(1) -> cannot use python min()function because it is O(n) to find min 
    '''
    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            minVal = min(self.minStack[-1], val)
            self.minStack.append(minVal)
        return 

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        return
    
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()