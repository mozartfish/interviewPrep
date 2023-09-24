class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L, R = 0, 1 
        res, prev = 1, ""
        while R < len(arr):
            if arr[R - 1]  > arr[R] and prev != ">":
                res = max(res, R - L + 1)
                R += 1 
                prev = ">"
            elif arr[R - 1] < arr[R] and prev != "<":
                res = max(res, R - L + 1)
                R += 1 
                prev = "<"
            else:
                if arr[R] == arr[R - 1]:
                    R += 1 
                else:
                    R = R 
                L = R - 1
                prev = ""
        return res


        