class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        l = 0 

        char_idx = {}

        seen = set()
        max_len = 0 
        
        for i in range(len(s)): 
            if s[i] in char_idx:
                l = max(char_idx[s[i]] + 1, l)


            char_idx[s[i]]= i
            max_len = max(max_len, i-l+1)

        
        return max_len 