class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0 
        L = 0 
        R = len(height) - 1 
        leftMax = height[L]
        rightMax = height[R]
        result = 0 
        while L < R:
            if leftMax < rightMax:
                L += 1 
                leftMax = max(leftMax, height[L])
                result += leftMax - height[L]
            else:
                R -= 1 
                rightMax = max(rightMax, height[R])
                result += rightMax - height[R]
        
        return result