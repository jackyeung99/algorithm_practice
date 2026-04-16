class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        


        dp = [[0] * len(text2) for _ in range(len(text1))]

    

        for row in range(len(dp)):
            for col in range(len(dp[0])): 
                
                top = 0 
                left = 0 
                tleft = 0 

                if row-1 >= 0 and col-1 >= 0:
                    tleft = max(top, dp[row-1][col-1])
                
                if row-1 >= 0:
                    top = max(top, dp [row-1][col])

                if col-1 >= 0:
                    left = max(left, dp[row][col-1]) 
                
                

                if text1[row] == text2[col]:
                    dp[row][col] = max(left, top, tleft+1)
                else:
                    dp[row][col] = max(left, top, tleft)




            


        return dp[-1][-1]