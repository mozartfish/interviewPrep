class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create a heap for sorted order 
        # python implements min heap so we need a max heap
        maxStones = [-s for s in stones]
        heapq.heapify(maxStones)

        while len(maxStones) > 1:
            s1 = heapq.heappop(maxStones)
            s2 = heapq.heappop(maxStones)
            if s2 > s1:
                heapq.heappush(maxStones, s1 - s2)
        
        # if all the stones are broken, return 0 
        maxStones.append(0)

        return abs(maxStones[0])

        