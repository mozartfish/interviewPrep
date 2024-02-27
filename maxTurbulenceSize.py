class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxLen = 1 
        L = 0
        R = 1 
        prevSign = ""
        while R < len(arr):
            # greater than 
            if arr[R - 1] > arr[R] and prevSign != ">":
                maxLen = max(maxLen, R - L + 1)
                R += 1 
                prevSign = ">"
                # pass 
            # less than 
            elif arr[R - 1] < arr[R] and prevSign != "<":
                maxLen = max(maxLen, R - L + 1)
                R += 1 
                prevSign = "<"
                # pass 
            # equal 
            else:
                if arr[R - 1] == arr[R]:
                    R += 1 
                # update L pointer after updating R pointer (for all cases)
                L = R - 1 
                prevSign = ""
        return maxLen 
        