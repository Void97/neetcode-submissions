class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 0
        max_profit = 0
        n = len(prices)
        
        for sell in range(n):
            if prices[buy] < prices[sell]:
                max_profit = max(max_profit, prices[sell] - prices[buy])
            else:
                buy = sell
        
        return max_profit