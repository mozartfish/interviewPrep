class SegmentTree:
    def __init__(self, total, L, R):
        self.sum = total 
        self.left = None 
        self.right = None 
        self.L = L 
        self.R = R 
    

class NumArray:
    def build(self, nums, L, R):
        if L == R:
            return SegmentTree(nums[L], L, R)
        M = (L + R) // 2 
        root = SegmentTree(0, L, R)
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum 
        
        return root 
    
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)
    
    def updateHelper(self, root, index, val):
        if root.L == root.R:
            root.sum = val 
            return 
        M = (root.L + root.R) // 2 
        if index > M:
            self.updateHelper(root.right, index, val)
        else:
            self.updateHelper(root.left, index, val)
        root.sum = root.left.sum + root.right.sum

    def update(self, index: int, val: int) -> None:
        self.updateHelper(self.root, index, val)

    def queryHelper(self, root, L, R):
        if L == root.L and R == root.R:
            return root.sum 
        M = (root.L + root.R) // 2 
        if L > M:
            return self.queryHelper(root.right, L, R)
        elif R <= M:
            return self.queryHelper(root.left, L, R)
        else:
            return (self.queryHelper(root.left, L, M) + 
            self.queryHelper(root.right, M + 1, R))

    def sumRange(self, left: int, right: int) -> int:
        return self.queryHelper(self.root, left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)