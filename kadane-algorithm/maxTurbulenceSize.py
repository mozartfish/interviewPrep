class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        '''
        - return the length of the maximum size turbulent subarray of arr 
        - a subarray is turbulent iff its signs 
        - need to somehow keep track of previous sign
        '''
        L = 0
        R = 1 
        maxLen = 1 
        prevSign = ""
        while R < len(arr):
            # greater than case 
            if arr[R - 1] > arr[R] and prevSign != ">":
                maxLen = max(maxLen, R - L + 1)
                R += 1 
                prevSign = ">"
            # less than case 
            elif arr[R - 1] < arr[R] and prevSign != "<":
                maxLen = max(maxLen, R - L + 1)
                R += 1 
                prevSign = "<"
            # equal case 
            else:
                if arr[R - 1] == arr[R]:
                    R += 1 
                # update left pointer after updating right pointer 
                L = R - 1
                prevSign = ""


        return maxLen



