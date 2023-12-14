class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L = 0 
        R = 1 
        maxLen = 1 
        prevSign = ""

        while R < len(arr):
            # Greater Than Case 
            if arr[R - 1] > arr[R] and prevSign != ">":
                maxLen = max(maxLen, R - L + 1)
                R += 1 
                prevSign = ">"
            # Less Than Case 
            elif arr[R - 1] < arr[R] and prevSign != "<":
                maxLen = max(maxLen, R - L + 1) 
                R += 1 
                prevSign = "<"
            else:
                # consecutive terms or equals sign 
                if arr[R - 1] == arr[R]:
                    R += 1 
                # update window if we update the right pointer 
                L = R - 1 
                prevSign = ""
        return maxLen
