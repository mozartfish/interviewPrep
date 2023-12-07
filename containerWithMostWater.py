class Solution:
    def maxArea(self, height: List[int]) -> int:
      '''
      - maximize volume of water -> looking for longest width 
      - take minimum of heights and find max distance 
      '''
      L = 0
      R = len(height) - 1 
      result = 0 
      while L < R:
        # calculate max volume 
        result = max(result, min(height[L], height[R]) * (R - L))
        # move pointers based on height at index L and index R
        if height[L] < height[R]:
          L += 1 
        elif height[R] <= height[L]:
          R -= 1 
      return result 
