
import  re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        strings  = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        l = 0
        r = len(strings) - 1


        while l < r:

            if strings[l] == strings[r][::- 1]:
                l += 1
                r -= 1
            
            else:
                return False

        return True
