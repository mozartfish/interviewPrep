# runtime - O(n) where n represents the total number of nodes in linked list 
# space - no additional space added per node on call stack 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # previous node tracker 
        next = None # keep track of next node 
        curr = head # keep track of the head 

        while curr:
            next = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next 
        return prev