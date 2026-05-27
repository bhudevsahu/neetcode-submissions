class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit > 0:
                maxP = max(profit, maxP)
            else:
                l = r
        
        return maxP