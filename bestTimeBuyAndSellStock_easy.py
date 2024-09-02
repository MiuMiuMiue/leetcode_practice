from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = -1
        maxPrice = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            if prices[i] <= maxPrice:
                profit = max(profit, maxPrice - prices[i])
            else:
                maxPrice = prices[i]

        return profit if profit > 0 else 0