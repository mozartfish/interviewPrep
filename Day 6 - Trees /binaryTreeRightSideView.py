# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        result = []
        q = deque() 

        # bfs algorithm 
        if root:
            q.append(root)
        while len(q) > 0:
            rightNode = None 
            for i in range(len(q)):
                curr = q.popleft()
                rightNode = curr 
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if rightNode:
                result.append(rightNode.val)

        return result 
        