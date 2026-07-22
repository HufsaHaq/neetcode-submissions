class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buying = 0
        selling = 1
        max_profit = 0
        while selling < len(prices):
            profit = prices[selling] - prices[buying] 
            max_profit = max(max_profit, profit)
            if prices[selling] < prices[buying]:
                buying = selling
            selling += 1
            

        return max_profit

        