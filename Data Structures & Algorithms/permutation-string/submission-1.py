class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        letter_counts = {}


        l = 0 
        win_size = len(s1)
        
        for r in range(0, len(s2)- win_size + 1): 
            
            window = s2[r:r+win_size]
            print(window)
            if ''.join(sorted(window)) == ''.join(sorted(s1)):
                return True

        return False