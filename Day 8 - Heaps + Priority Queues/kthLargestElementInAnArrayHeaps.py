class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxNums = [-n for n in nums]
        heapq.heapify(maxNums)
        result = -1 
        while k > 0:
            result = heapq.heappop(maxNums)
            k -= 1 
        return result * -1