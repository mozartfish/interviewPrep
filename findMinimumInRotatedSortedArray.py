class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        if 
        nums[mid] >= nums[L]
        else search left half 
        '''
        lo = 0 
        hi = len(nums) - 1 
        result = nums[0]

        while lo <= hi:
            if nums[lo] < nums[hi]:
                result = min(result, nums[lo])
                break 

            mid = (lo + hi)//2 
            result = min(result, nums[mid])
            if nums[mid] >= nums[lo]:
                lo = mid + 1 
            else:
                hi = mid - 1 
        
        return result 


            