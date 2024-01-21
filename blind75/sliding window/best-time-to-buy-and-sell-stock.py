from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        profit = 0
        for i in prices:
            minp = min(minp, i)
            profit = max(profit, i-minp)
        return profit