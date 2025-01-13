from typing import List 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]

        return max_profit
    def maxProfit_s1(self, prices: List[int]) -> int:

        n = len(prices)
        if n < 2: return 0
        i = 1
        buy_price = prices[0]
        while i < n:
            if buy_price > prices[i]:
                buy_price = prices[i]
                i += 1
                continue
            break
        if i == n: return 0
        self.good_profits = [-1] * n 
        return self.find_profit(prices, i-1, n-1)

    def find_profit(self, prices: List[int], first_day: int, last_day: int) -> int:
        if first_day > last_day: return 0
        if self.good_profits[first_day] > -1: return self.good_profits[first_day]
        good_profit = 0

        buy_price = float('inf')
        
        for day in range(first_day, last_day+1):
            if buy_price > prices[day]: 
                buy_price = prices[day]
                continue
            diff_price = prices[day] - buy_price
            if diff_price > 0:
                possible_profit = diff_price + self.find_profit(prices, day+1, last_day) 
                if possible_profit > good_profit:
                    good_profit = possible_profit
        self.good_profits[first_day] = good_profit
        return good_profit
