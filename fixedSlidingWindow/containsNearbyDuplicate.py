class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numMap = {} 
        for indx, num in enumerate(nums):
            if num in numMap and abs(indx - numMap[num]) <= k:
                return True 
            else:
                numMap[num] = indx 
        return False 
        