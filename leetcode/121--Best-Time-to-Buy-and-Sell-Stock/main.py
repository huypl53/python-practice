from typing import List, Tuple

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0
        for i in range(0, n-1):
            if prices[i] < prices[i+1]: break
        else: return 0
        
        for j in range(n-1, 0, -1):
            if prices[j] > prices[j-1]: break
        else: return 0
        if i >= j: return 0
        
        min_price = prices[i]
        best_deal= 0
        for k in range(1, j-i+1):
            min_price = min(min_price, prices[k+i])
            best_deal = max(best_deal, prices[k+i] - min_price)
        # print(best_deal, min_price)
        return best_deal
