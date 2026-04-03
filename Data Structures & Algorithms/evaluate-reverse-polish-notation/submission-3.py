import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        val = []

        
        for i in tokens: 
            if i in ['+', '-', '*', '/']:
                val2 = val.pop(-1)
                val1 = val.pop(-1)
                if i == '+': 
                    val.append(val1 + val2)
                elif i == '-':
                    val.append(val1 - val2)
                elif i == '*':
                    val.append(val1 * val2)
                else: 
                    val.append(int(float(val1)/val2))
            else:
                val.append(int(i))

        return val[-1]
