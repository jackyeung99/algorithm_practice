class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        for i in asteroids: 

            
            # no collision 
            if not stack or abs(i + stack[-1]) == abs(i) + abs(stack[-1]) or stack[-1] < 0 and i > 0:
                stack.append(i)
                continue
            
            alive = True
            while alive and stack and (stack[-1] > 0 and i < 0):
                if abs(i) == abs(stack[-1]):
                    stack.pop()
                    alive = False
                
                elif abs(i) < abs(stack[-1]): 
                    alive = False
        
                else:
                    stack.pop()

            if alive:
                stack.append(i)




        return stack 