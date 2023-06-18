# runtime - same runtime for linked list operations 
# space time - no additional space added for each element 
class ListNode:
    def __init__(self, value, prev=None):
        self.next = None 
        self.prev = prev 
        self.val = value 

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        

    def visit(self, url: str) -> None:
        self.head.next = ListNode(url, self.head)
        self.head = self.head.next 
        return 
        
    def back(self, steps: int) -> str:
        while self.head.prev and steps > 0:
            self.head = self.head.prev 
            steps -= 1
        
        return self.head.val
        

    def forward(self, steps: int) -> str:
        while self.head.next and steps > 0:
            self.head = self.head.next 
            steps -=1 
        
        return self.head.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)