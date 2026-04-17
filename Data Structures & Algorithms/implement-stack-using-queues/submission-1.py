class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None
        self.prev = None 


class MyStack:

    def __init__(self):
        self.head = None 
        self.tail = None
        

    def push(self, x: int) -> None:
        node = Node(x)

        if self.tail:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node  
        else:
            self.head = node 
            self.tail = node 


    def pop(self) -> int:
        if self.tail:
            last = self.tail
            self.tail = last.prev

            if not self.tail:
                self.head = None 
                
            return last.val

        return None


    def top(self) -> int:
        if self.tail:
            return self.tail.val
        
        return None 

    def empty(self) -> bool:
        print(self.head, self.tail)
        return True if self.head is None else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()