class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        '''
        - return number of subarrays of size k and average >= threshold 
        - subarrays of size k indicates we need a fixed sliding window
        '''
        result = 0
        currSum = sum(arr[:k - 1])

        for L in range(len(arr) - k + 1):
            currSum += arr[L + k - 1]
            if (currSum // k) >= threshold:
                result += 1 
            currSum -= arr[L]
        
        return result 