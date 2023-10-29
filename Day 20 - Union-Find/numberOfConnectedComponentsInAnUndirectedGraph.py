class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {} 
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 1 
    
    def find(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            # path compression
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p 
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1 
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2 
        else:
            self.parent[p1] = p2 
            self.rank[p2] += 1 
        
        return True 
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for n1, n2 in edges:
            uf.union(n1, n2)
        
        result = set()
        for i in range(n):
            result.add(uf.find(i))
            
        return len(result)