class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0 for i in range(n * 2)]
        for i in range(n):
            result[i] = nums[i]
            result[i + n] = nums[i]
        
        return result

# runtime - O(n) where n represents the number of elements in nums