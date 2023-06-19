# runtime - O(n^2)
# space - constant since no extra memory used 
# stability - unstable sort 
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            minIndx = i 
            for j in range(i + 1, n):
                if nums[j] < nums[minIndx]:
                    minIndx = j
            nums[minIndx], nums[i] = nums[i], nums[minIndx]
        
        return nums