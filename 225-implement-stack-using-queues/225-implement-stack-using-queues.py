class MyStack:

    def __init__(self):
        self.que1 = deque([])
        self.que2 = deque([])
    def push(self, x: int) -> None:
        self.que1.append(x)
        self.que2 = deque([x])
        

    def pop(self) -> int:
        
        t = self.que2.popleft()
        v = t
        while len(self.que1) > 1:
            v =self.que1.popleft()
            self.que2.append(v)
        self.que1 = deque([])
        while self.que2:
            self.que1.append(self.que2.popleft())
        print(self.que1)
        if self.que1:
            self.que2.append(v)
        return t

    def top(self) -> int:
        return self.que2[0]

    def empty(self) -> bool:
        return not self.que2
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()