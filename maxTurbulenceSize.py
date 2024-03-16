# Longest Turbulent Subarray 
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxLen = 1 
        prevSign = ""
        L = 0 
        R = 1 
        while R < len(arr):
            # greater than 
            if arr[R - 1] > arr[R] and prevSign != ">":
                maxLen = max(maxLen, R - L + 1)
                R += 1 
                prevSign = ">"
            # less than 
            elif arr[R - 1] < arr[R] and prevSign != "<":
                maxLen = max(maxLen, R - L + 1)
                R += 1
                prevSign = "<"
            # equal
            else:
                if arr[R - 1] == arr[R]:
                    R += 1 
                # update L pointer after updating R pointer (all cases)
                L = R - 1 
                prevSign = ""
        return maxLen 
        