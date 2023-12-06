# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # find the smalles value in the BST (linkedlist traversal)
    def findMin(self, root):
        curr = root 
        while curr and curr.left:
            curr = curr.left
        return curr 

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # base case 
        if not root:
            return None 
        
        # recursive case 
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        # we find the node we want to delete 
        else:
            # 0 or 1 children 
            # no left children 
            if not root.left:
                return root.right 
            # no right children 
            elif not root.right:
                return root.left 
            # 2 children 
            else:
                # find the min node of the right subtree 
                minNode = self.findMin(root.right)
                # update the current roots value 
                root.val = minNode.val
                # remove the duplicate value 
                root.right = self.deleteNode(root.right, minNode.val)
            
        return root
