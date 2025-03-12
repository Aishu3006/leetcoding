class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyingPrice = prices[0]

        for price in prices:
            buyingPrice = min(buyingPrice, price)
            profit = price - buyingPrice
            maxProfit = max(maxProfit, profit)
        
        return maxProfit