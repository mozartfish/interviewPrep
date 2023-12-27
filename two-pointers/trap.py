class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        - maximize the amount of water on the left hand side 
        - maximize the amount of water on the right hand side 
        - compute total water by adding water on the left and water on the right
        '''
        L = 0
        R = len(height) - 1 
        leftMax = height[L]
        rightMax = height[R]
        result = 0

        # edge case - check for empty list 
        if len(height) == 0:
            return 0 

        while L < R:
            if leftMax < rightMax:
                L += 1 
                leftMax = max(leftMax, height[L])
                result += (leftMax - height[L])
            else:
                R -= 1 
                rightMax = max(rightMax, height[R])
                result += (rightMax - height[R])
        return result 

