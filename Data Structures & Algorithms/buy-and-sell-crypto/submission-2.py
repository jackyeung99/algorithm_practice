class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        

        # brute force solution 
            # max_price = 0 


            # for i in range(len(prices)):
            #     for j in range(i, len(prices)):
            #         max_price = max(max_price, prices[j] - prices[i])


            # return max_price


        # Optimized sliding window 

        max_price = 0 

        r = 1
        l = 0 

        while r < len(prices):
            if prices[l] < prices[r]:
                max_price = max(max_price, prices[r] - prices[l])
            else:
                l = r 

            r += 1
            
        return max_price






