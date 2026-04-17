class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []

        for op in operations:

            if op == 'C':
                stack.pop()

            elif op == 'D': 
                stack.append(stack[-1] * 2)
                

            elif op =='+':
                
                score_1 = stack[-1]
                score_2 = stack[-2]

                stack.append(score_1 + score_2)
                pass

            else:
                stack.append(int(op))


        return sum(stack)