# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bfs 
        # from collections import deque 
        # if not root:
        #     return 0 
        
        # q = deque() 
        # level = 0
        # q.append(root)

        # while len(q) > 0:
        #     for i in range(len(q)):
        #         curr = q.popleft() 
        #         if curr.left:
        #             q.append(curr.left)
        #         if curr.right:
        #             q.append(curr.right)
            
        #     level += 1
        # return level 

        # dfs 
        if not root:
            return 0 
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

