class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {} 
        # number of ways to climb 0 steps 
        cache[0] = 1 
        
        # number of ways to climb 1 steps 
        cache[1] = 1 

        for i in range(2, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
        
        return cache[n]