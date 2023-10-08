class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visited = set() 

        # dfs helper function 
        def dfs(crs):
            if crs in visited:
                return False 
            if preMap[crs] == []:
                return True 
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False 
            # finished visiting all the nodes for a particular path 
            visited.remove(crs)
            preMap[crs] = []
            return True
        
        # main algorithm 
        for crs in range(numCourses):
            if not dfs(crs):
                return False 
        
        return True 