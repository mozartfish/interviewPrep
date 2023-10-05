class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxWeight = [-s for s in stones]
        heapq.heapify(maxWeight)
        while len(maxWeight) > 1:
            s1 = heapq.heappop(maxWeight)
            s2 = heapq.heappop(maxWeight)
            if s2 > s1:
                heapq.heappush(maxWeight, s1- s2)
        maxWeight.append(0)
        return abs(maxWeight[0])
        