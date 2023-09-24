# runtime - O(log n)
# space - constant - no additional memory used

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinNode(self, root):
        curr = root 
        while curr and curr.left:
            curr = curr.left
        return curr


    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None 
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # 0 or 1 children 
            if not root.left:
                return root.right 
            elif not root.right:
                return root.left
            else:
                # 2 or more children 
                minNode = self.findMinNode(root.right)
                root.val = minNode.val 
                root.right = self.deleteNode(root.right, minNode.val)
        
        return root


            