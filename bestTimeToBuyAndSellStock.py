class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      '''
      - greedy algorithm approach
      '''
      maxProfit = 0
      minPrice = prices[0]

      for p in prices:
        # update minPrice to create have a profit >= 0
        if p < minPrice:
          minPrice = p 
        # calculate maximum profit for price p 
        maxProfit = max(maxProfit, p - minPrice)
      return maxProfit
        