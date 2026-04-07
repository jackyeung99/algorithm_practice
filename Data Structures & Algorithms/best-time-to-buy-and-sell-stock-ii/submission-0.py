class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0 
        cur_max =  0
        for day in range(len(prices) -1, -1, -1):
            if prices[day] < cur_max:
                profit += cur_max - prices[day]
                cur_max = prices[day]
            else: 
                cur_max = max(cur_max, prices[day])

        return profit