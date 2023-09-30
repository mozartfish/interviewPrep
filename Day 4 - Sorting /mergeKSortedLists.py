# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeLists(self, l1, l2):
        result = ListNode(-1)
        dummy = result
        while l1 and l2:
            if l1.val < l2.val:
                result.next = l1 
                l1 = l1.next 
                result = result.next 
            else:
                result.next = l2
                l2 = l2.next 
                result = result.next 
        if l1:
            result.next = l1 
        if l2:
            result.next = l2  
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None 
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None 
                mergedLists.append(self.mergeLists(l1, l2))
            lists = mergedLists 
        return lists[0]