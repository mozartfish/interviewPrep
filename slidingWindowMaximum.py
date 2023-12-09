class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque 
        output = []
        q = deque()
        L = R = 0 

        while R < len(nums):
            # pop smaller values from Q 
            while q and nums[q[-1]] < nums[R]:
                q.pop() 
            q.append(R)

            # remove left value from window 
            if L > q[0]:
                q.popleft() 

            if (R + 1) >= k:
                output.append(nums[q[0]])
                L += 1 
            R += 1  
        
        return output 