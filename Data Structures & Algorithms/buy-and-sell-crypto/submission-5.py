class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        j = 0
        max_profit = 0
        
        for i in range(len(prices)):
            if prices[j] < prices[i]:
                profit = prices[i] - prices[j]
                max_profit = max(max_profit, profit)
            else:
                j = i

        return max_profit
        