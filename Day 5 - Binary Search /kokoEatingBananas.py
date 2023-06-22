# runtime - O(n log w) where w is the max bananas from all piles 
# space - constant since no other memory needed 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1 
        hi = max(piles)
        result = hi 

        while lo <= hi:
            hours = 0
            k = (lo + hi) // 2 
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours <= h:
                result = min(result, k)
                hi = k - 1 
            else:
                lo = k + 1

        return result 