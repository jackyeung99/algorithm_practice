class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        if amount == 0:
            return 0 

        # if len(coins) <2:
        #     return 1 if coins[0] == amount else -1


        dp = [float('inf')] * (amount)

        for coin in coins:
            if coin -1 < amount:
                dp[coin-1] = 1

    
        for i in range(amount):
            min_jump = dp[i]
            
            for coin in coins:
                if i - coin >= 0:
                    min_jump = min(min_jump, dp[i-coin] + 1)

            dp[i] = min_jump


        if dp[-1] == float('inf'):
            return -1 
        else:
            return dp[-1]