# - Keep track of nodes connected in a graph 
# - Detect Cycles in a graph 
# - Operate on Disjoint Sets -> sets that don't have any common elements
# - Complexity: O(m * logn)
class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 1 

    # Take a vertex n and return its parent vertex 
    def find(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            # path compression
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        
        return p
    
    # Take two vertices and determine if a union can be performed
    # If two vertices share the same parent a union cannot be formed
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.din(n2)
        # detect a cycle 
        if p1 == p2:
            return False 
        
        # Union by Rank
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1 
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2 
        else:
            self.parent[p1] = p2 
            self.rank[p2] += 1 
        
        return True 
    
