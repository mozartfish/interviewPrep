# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # base case 
        if not root:
            return None 
        # recursive step 
        if val < root.val:
            root = self.searchBST(root.left, val)
        elif val > root.val:
            root = self.searchBST(root.right, val)
        return root