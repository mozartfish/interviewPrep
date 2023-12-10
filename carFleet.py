class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        - go through car list in reverse sorted order 
        - compare adjacent cars on the stack to see if they collide using speed 
        '''
        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []

        # iterate in reverse sorted order 
        for p, s in sorted(pairs)[::-1]:
            stack.append((target - p) / s)
            # check for collisions 
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)