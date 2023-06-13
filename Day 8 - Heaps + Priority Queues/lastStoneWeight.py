class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStones = [-s for s in stones]
        heapq.heapify(maxStones)
        while len(maxStones) > 1:
            s1 = heapq.heappop(maxStones)
            s2 = heapq.heappop(maxStones)
            if s2 > s1:
                heapq.heappush(maxStones, s1 - s2)
        maxStones.append(0)
        return abs(maxStones[0])