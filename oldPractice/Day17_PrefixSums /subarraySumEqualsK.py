class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefixSum -> count 
        result = 0
        currSum = 0
        prefixSums = {0: 1}
        for n in nums:
            currSum += n 
            diff = currSum - k 
            result += prefixSums.get(diff, 0)
            prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)
        return result