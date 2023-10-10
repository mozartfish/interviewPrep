class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        right = 1 
        maxLen = 1 
        prevSign = ""

        while right < len(arr):
            if arr[right - 1] > arr[right] and prevSign != ">":
                maxLen = max(maxLen, right - left + 1)
                right += 1 
                prevSign = ">"
            elif arr[right - 1] < arr[right] and prevSign != "<":
                maxLen = max(maxLen, right - left + 1)
                right += 1 
                prevSign = "<"
            else:
                # handle equal signs 
                if arr[right] == arr[right - 1]:
                    right += 1 
                else:
                    right = right 
                left = right - 1 
                prevSign = ""

        return maxLen
