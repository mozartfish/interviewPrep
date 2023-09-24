# runtime - O(n)in average case, O(n^2) in worst case 
# space - constant since no additional memroy used 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k 
        def quickSelect(left, right):
            pivot, p = nums[right], left 
            # partition 
            for i in range(left, right):
                if nums[i] < pivot:
                    temp = nums[p]
                    nums[p] = nums[i]
                    nums[i] = temp 
                    p += 1 
            nums[p], nums[right] = nums[right], nums[p]
            if k > p:
                return quickSelect(p + 1, right)
            elif k < p:
                return quickSelect(left, p - 1)    
            else:
                return nums[p]
        return quickSelect(0, len(nums) - 1)