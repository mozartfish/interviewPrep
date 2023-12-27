class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        - given an array of heights of length n 
        - n vertical lines such that ith line is (i, 0) and (i, height[i])
        - find two lines (1 pair) that together with x-axis form a container that stores the maximum water 
        - return the amount of water a container can store
        - max water = max area of rectangle -> max(length * width)
        '''

        L = 0
        R = len(height) - 1
        result = 0

        while L < R:
            # calculate max water 
            result = max(result, min(height[L], height[R]) * (R - L))
            # move pointers based on the height at index L and index R 
            if height[L] < height[R]:
                L += 1 
            elif height[R] <= height[L]:
                R -= 1 
        
        return result 
        