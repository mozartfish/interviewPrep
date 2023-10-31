class SegmentTree:
    def __init__(self, total, L, R) -> None:
        self.sum = total 
        self.left = None 
        self.right = None 
        self.L = L 
        self.R = R 
    
    def build(nums, L, R):
        if L == R:
            return SegmentTree(nums[L], L, R)
        
        # split the range in half
        M = (L + R) // 2

        # calculate the sume at each node and return the overall sum 
        root = SegmentTree(0, L, R)
        root.left = SegmentTree.build(nums, L, M)
        root.right = SegmentTree.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum 
        
        return root 
    
    # update a node sum
    def update(self, index, val):
        if self.L == self.R:
            self.sum = val
            return

        M = (self.L + self.R) // 2

        if index > M:
            self.right.update(index, val)
        else:
            self.left.update(index, val)
        self.sum = self.left.sum + self.right.sum


    def rangeQuery(self, L, R):
        if L == self.L and R == self.R:
            return self.sum

        M = (self.L + self.R) // 2
        if L > M:
            return self.right.rangeQuery(L, R)
        elif R <= M:
            return self.left.rangeQuery(L, R)
        else:
            return (self.left.rangeQuery(L, M) +
                    self.right.rangeQuery(M + 1, R))
