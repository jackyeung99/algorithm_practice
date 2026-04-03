from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        

        char_map = {
            ")": "(", 
            "]": "[", 
            "}": "{"
        }


        st = []
        for i in s:
            if len(st) == 0 or i not in char_map:
                st.append(i) 
                continue 
                
            if st[-1] == char_map[i]:
                st.pop()
            else:
                st.append(i)




        return len(st) == 0

