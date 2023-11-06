# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]
        def dfs(root):
            # if the subtree is null or is a leaf node 
            if not root:
                return -1 
            # update the diameter
            left = dfs(root.left)
            right = dfs(root.right)
            result[0] = max(result[0], left + right + 2)

            # return the height for computing the diameter in the next level 
            return 1 + max(left, right)

        dfs(root)
        return result[0]