class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L = 0
        R = 1 
        maxLen = 1 
        prevSign = ""

        while R < len(arr):
            if arr[R - 1] > arr[R] and prevSign != ">":
                maxLen = max(maxLen, R - L + 1)
                R += 1 
                prevSign = ">"
            elif arr[R - 1] < arr[R] and prevSign != "<":
                maxLen = max(maxLen, R - L + 1)
                R += 1 
                prevSign = "<"
            else:
                # consecutive signs or equals
                if arr[R] == arr[R - 1]:
                    R += 1 
                # update the window if we update the right pointer
                L = R - 1 
                prevSign = ""
        return maxLen
        