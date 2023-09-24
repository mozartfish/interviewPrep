# runtime - O(n) since we hae to traverse every single node in the tree
# space - O(n) due to recursive call stack 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        k = k - 1 
        result = [] 
        def DFS(root):
            if not root:
                return 
            DFS(root.left)
            result.append(root.val)
            DFS(root.right)
        
        DFS(root)
        return result[k]