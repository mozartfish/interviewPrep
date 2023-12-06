class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # set up union find 
        n = len(edges)
        parent = {}
        rank = {}
        for i in range(1, n + 1):
            parent[i] = i 
            rank[i] = 1
        
        # take a vertex and find if parent can be found
        def find(n):
            p = parent[n]
            while p!= parent[p]:
                # path compression 
                 parent[p] = parent[parent[p]]
                 p = parent[p]
            return p 
        
        # take two vertices and determine if union can be performed 
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            # cycle detection
            if p1 == p2:
                return False 
            
            # Union by Rank
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p2] < rank[p1]:
                parent[p1] = p2 
            else:
                parent[p1] = p2 
                rank[p2] += 1 

            return True 
            
        # main algorithm 
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        return []