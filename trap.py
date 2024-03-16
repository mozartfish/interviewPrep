# Trapping Rain Water 
class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        totalWater = 0
        leftMax = height[L]
        rightMax = height[R] 

        if len(height) == 0:
            return 0 
        
        while L < R:
            if leftMax < rightMax:
                L += 1 
                leftMax = max(leftMax, height[L])
                totalWater += (leftMax - height[L])
            else:
                R -= 1 
                rightMax = max(rightMax, height[R])
                totalWater += (rightMax - height[R])

        return totalWater 

        