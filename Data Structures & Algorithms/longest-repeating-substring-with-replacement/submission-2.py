class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        char_window = {}

        l = 0
        
        max_win = 0
        maxf = 0

        for r in range(len(s)): 


            char_window[s[r]] = char_window.get(s[r], 0) + 1 

            maxf = max(maxf, char_window[s[r]])
           
            while (r-l + 1) - maxf > k  : 
                char_window[s[l]] -= 1 
                l += 1

            max_win = max(max_win, r-l+1)


        return max_win
        
            

            
            

