# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # check if two trees are the same tree 
    def sameTree(self, p, q):
        # base case 
        if not p and not q:
            return True 
        
        if not p or not q or p.val != q.val:
            return False 
        
        # recursive case - check left and right trees 
        return (self.sameTree(p.left, q.left) and 
        self.sameTree(p.right, q.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # tree is a subtree of itself 
        if root and not subRoot:
            return True 
        
        # tree does not exist 
        if not root:
            return False 
        
        # check if tree and subtree match 
        if self.sameTree(root, subRoot):
            return True 
        
        # recursively check the left and right branches 
        return (self.isSubtree(root.left, subRoot) or 
        self.isSubtree(root.right, subRoot))
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # check if two trees are the same tree 
    def sameTree(self, p, q):
        # base case 
        if not p and not q:
            return True 
        
        if not p or not q or p.val != q.val:
            return False 
        
        # recursive case - check left and right trees 
        return (self.sameTree(p.left, q.left) and 
        self.sameTree(p.right, q.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # tree is a subtree of itself 
        if root and not subRoot:
            return True 
        
        # tree does not exist 
        if not root:
            return False 
        
        # check if tree and subtree match 
        if self.sameTree(root, subRoot):
            return True 
        
        # recursively check the left and right branches 
        return (self.isSubtree(root.left, subRoot) or 
        self.isSubtree(root.right, subRoot))
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # check if two trees are the same tree 
    def sameTree(self, p, q):
        # base case 
        if not p and not q:
            return True 
        
        if not p or not q or p.val != q.val:
            return False 
        
        # recursive case - check left and right trees 
        return (self.sameTree(p.left, q.left) and 
        self.sameTree(p.right, q.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # tree is a subtree of itself 
        if root and not subRoot:
            return True 
        
        # tree does not exist 
        if not root:
            return False 
        
        # check if tree and subtree match 
        if self.sameTree(root, subRoot):
            return True 
        
        # recursively check the left and right branches 
        return (self.isSubtree(root.left, subRoot) or 
        self.isSubtree(root.right, subRoot))
        