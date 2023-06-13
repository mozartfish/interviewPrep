# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minNode(self, root):
        curr = root 
        while curr and curr.left:
            curr = curr.left
        return curr
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # base case 
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # case 1: 0 or 1 children 
            if not root.left:
                return root.right 
            elif not root.right:
                return root.left
            else:
                # case 2 -> two children
                minNode = self.minNode(root.right)
                root.val = minNode.val 
                root.right = self.deleteNode(root.right, minNode.val)
        
        return root

        