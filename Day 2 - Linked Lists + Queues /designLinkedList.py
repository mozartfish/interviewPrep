# runtime - same runtime for linked list operations 
# space time - no additional space added for each element 
class ListNode:
    def __init__(self, value=-1):
        self.next = None 
        self.val = value 

class MyLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.size = 0 

    def get(self, index: int) -> int:
        if index < 0 or index >=self.size:
            return -1 
        curr = self.head
        for i in range(index + 1):
            curr = curr.next
        return curr.val 
        
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        return 

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        return 
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        if index < 0:
            index = 0
        curr = self.head 
        for i in range(index):
            curr = curr.next 
        newNode = ListNode(val)
        newNode.next = curr.next 
        curr.next = newNode 
        self.size += 1 
        return 

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return 
        curr = self.head 
        for i in range(index):
            curr = curr.next 
        curr.next = curr.next.next 
        self.size -= 1 
        return 
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)