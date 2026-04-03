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


 
        for i in range(len(prices)):

            highest = i
            while highest+1 < len(prices) and  prices[highest+1] > prices[i]:
            
                highest += 1 
                max_price = max(max_price, prices[highest] - prices[i])

        return max_price






