class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        # keep track of the smallest minimum price to maximize profit 
        minPrice = prices[0]

        for p in prices:
            if p < minPrice:
                minPrice = p 
            maxProfit = max(maxProfit, p - minPrice)
        return maxProfit 