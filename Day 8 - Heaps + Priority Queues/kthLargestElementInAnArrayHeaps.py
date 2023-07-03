# runtime - O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        result = -1 
        while k > 0:
            result = heapq.heappop(nums)
            k -= 1 
        
        return result * -1
