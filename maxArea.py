# Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0 
        R = len(height) - 1 
        maxWater = 0 

        while L < R:
            maxWater = max(maxWater, min(height[L], height[R]) * (R - L))
            if height[L] < height[R]:
                L += 1 
            elif height[R] <= height[L]:
                R -= 1 
        
        return maxWater 

        