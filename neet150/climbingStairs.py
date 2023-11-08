class Solution:
    def climbStairs(self, n: int) -> int:
        # 0 steps - 1 way 
        # 1 step 
        # 2 steps 

        cache = {}
        cache[0] = 1 
        cache[1] = 1 

        for i in range(2, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
        
        return cache[n]