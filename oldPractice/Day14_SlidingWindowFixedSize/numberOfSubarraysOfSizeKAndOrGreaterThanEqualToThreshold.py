class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # keep track of current sum that is >= threshold 
        currSum = 0
        # keep track of the number of subarrays of size k whose sum is >= threshold 
        subCount = 0
        # pointers for keeping track of array position 
        L = 0
        R = 0
        while R < len(arr):
            currSum += arr[R]
            # check if less than size k 
            if R - L + 1 < k:
                R += 1 
            elif R - L + 1 == k:
                if currSum // k >= threshold:
                    subCount += 1 
                currSum -= arr[L]
                L += 1 
                R += 1 

        return subCount