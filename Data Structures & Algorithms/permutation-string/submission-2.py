class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        letter_counts = {}
        
        target_counts = {}
        for i in s1:
            target_counts[i] = target_counts.get(i, 0) + 1

        win = 0

        l = 0 
        win_size = len(s1)
        
        for r in range(0, len(s2)): 
        
            
            letter_counts[s2[r] ] = letter_counts.get(s2[r], 0) + 1
            print(letter_counts)
            win += 1
            if win > win_size:
                print(r, win_size)
                last_letter = s2[r-win_size] 
                letter_counts[last_letter] -= 1
                if letter_counts[last_letter] == 0:
                    del letter_counts[last_letter]

            if letter_counts == target_counts:
                return True
            

        return False