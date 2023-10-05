class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for x, y in points:
            dist = (x**2) + (y**2)
            heap.append([dist, x, y])
        heapq.heapify(heap)
        while k > 0:
            dist, x, y = heapq.heappop(heap)
            result.append([x, y])
            k -= 1 
        
        return result