# runtime - O(n)
# unstable sort 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        buckets = [0 for i in range(3)]

        for num in nums:
            buckets[num] += 1 
        
        i = 0 
        for j in range(len(buckets)):
            for k in range(buckets[j]):
                nums[i] = j 
                i += 1 
        
        return nums