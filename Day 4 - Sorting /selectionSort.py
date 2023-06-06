
# O(n ^2)
# - in place sort 
# - unstable
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            minIndx = i 
            for j in range(i + 1, n):
                if nums[j] < nums[minIndx]:
                    minIndx = j 
            nums[i], nums[minIndx] = nums[minIndx], nums[i]
        
        return nums
