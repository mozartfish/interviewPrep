class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for indx, val in enumerate(nums):
            # check for duplicates 
            if indx > 0 and val == nums[indx-1]:
                continue 
            # modified two sum 
            L = indx + 1 
            R = len(nums) - 1 
            while L < R:
                total = val + nums[L] + nums[R]
                if total > 0:
                    R -= 1 
                elif total < 0:
                    L += 1 
                else:
                    result.append([val, nums[L], nums[R]])
                    # move only one pointer 
                    L += 1 
                    # keep moving the left pointer if duplicate while left pointer < right pointer 
                    while nums[L] == nums[L-1] and L < R:
                        L += 1 
        
        return result 