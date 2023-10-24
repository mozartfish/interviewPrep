# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head 
        fast = head 
        prev = None 
        while fast and fast.next:
            fast = fast.next.next 
            temp = slow.next 
            slow.next = prev
            prev = slow 
            slow = temp 
        
        result = 0 
        while slow:
            result = max(result, prev.val + slow.val)
            prev = prev.next 
            slow = slow.next 
        
        return result 
