class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {} 

        for indx, num in enumerate(nums):
            diff = target - num
            if diff in numMap:
                return [indx, numMap[diff]]
            else:
                numMap[num] = indx 
        return []
        