class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_rectangle = 0

        stack = []
        for right, h in enumerate(heights):
    
            left = right
            while stack and h <= stack[-1][-1]:
                left, pre_height = stack.pop()
                max_rectangle = max(max_rectangle, pre_height * (right-left))
        
            
            stack.append((left, h))
        

        while stack: 
            left, pre_height = stack.pop()
            max_rectangle = max(max_rectangle, pre_height * (len(heights) - left))

        return max_rectangle
