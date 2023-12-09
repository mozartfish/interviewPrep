class Solution:
    def trap(self, height: List[int]) -> int:
      '''
      - can only store water if one of the heights is greater
      than the other 
      '''
      # edge case - check if we have empty height 
      if len(height) == 0:
        return 0 

      L = 0 
      R = len(height) - 1 
      result = 0
      leftMax = height[L]
      rightMax = height[R]

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