# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, totalSum):
            if not root:
                return False 
            
            totalSum += root.val 
            
            if not root.left and not root.right:
                return totalSum == targetSum 
            
            return dfs(root.left, totalSum) or dfs(root.right, totalSum)
        
        return dfs(root, 0)

