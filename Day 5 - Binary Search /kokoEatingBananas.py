class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1 
        hi = max(piles)
        result = hi 

        while lo <= hi:
            k = (lo + hi) // 2 
            hours = 0 
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours <= h:
                result = min(result, k)
                hi = k - 1 
            else:
                lo = k + 1 
        
        return result 
