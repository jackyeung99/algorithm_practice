class MinStack:

    def __init__(self):
        self.stack = []
        self.cur_min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append((val, min(self.cur_min, val) ))
        self.cur_min = min(self.cur_min, val) 

    def pop(self) -> None:
        val = self.stack.pop(-1)
        if len(self.stack) > 0: 
            self.cur_min = self.stack[-1][-1]
        else:
            self.cur_min = float('inf')
        return val[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return int(self.cur_min)

        
