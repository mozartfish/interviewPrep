class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {} 
        n = len(cost)
        for i in range(n):
            cache[i] = cost[i]
        cache[n] = 0
        
        for i in range(n - 3, -1, -1):
            cache[i] += min(cache[i + 1], cache[i + 2])
            print(cache[i])
        
        
        return min(cache[0], cache[1])