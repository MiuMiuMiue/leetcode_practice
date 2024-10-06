from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        localMin = 0
        totalProfit = 0

        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            localMin = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            totalProfit += prices[i] - localMin
        
        return totalProfit