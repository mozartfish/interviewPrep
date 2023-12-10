class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        - piles is counted in 1 based counting 
        - n piles of bananas 
        - guards check in h hours 
        - K - banana per hour eating speed 
        - chooses a random pile and chooses k bananas from that pile -> this is determining the mid from binary search 

        '''
        lo = 1 
        hi = max(piles)
        result = hi 

        while lo <= hi:
            # calculate eating speed for some pile 
            k = (lo + hi) // 2 
            hours = 0 
            for p in piles:
                # calculate hours from pile and eating speed 
                hours += math.ceil(p / k)
            if hours <= h:
                result = min(result, k)
                hi = k - 1
            else:
                lo = k + 1 

        return result 
        