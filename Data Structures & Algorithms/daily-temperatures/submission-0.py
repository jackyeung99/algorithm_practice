class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = [(temperatures[0], 0 )]
        for i in range(1, len(temperatures)):


            while True:
                if len(stack) < 1:
                    stack.append((temperatures[i], i))

                top = stack[-1]

                temp = top[0]
                idx = top[1]

                if temperatures[i] > temp:
                    res[idx] = i - idx
                    stack.pop(-1)
                else:
                    stack.append((temperatures[i], i))
                    break
                
                    


        return res