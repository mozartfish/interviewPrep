class MyStack:
    from collections import deque

    def __init__(self):
        self.stack = deque()
        

    def push(self, x: int) -> None:
        self.stack.appendleft(x)
        return
        

    def pop(self) -> int:
        return self.stack.popleft()
        

    def top(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        return not self.stack
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()