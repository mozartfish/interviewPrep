class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for indx, val in enumerate(nums):
            diff = target - val
            if diff in numMap:
                return [indx, numMap[diff]]
            else:
                numMap[val] = indx 
        
        return []
        