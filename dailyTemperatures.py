class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        - monotonically decreasing stack -> elements are in decreasing order from bottom to top of stack
        '''
        result = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIndex = stack.pop() 
                result[stackIndex] = (i - stackIndex)
            stack.append([t, i])
        
        return result 
