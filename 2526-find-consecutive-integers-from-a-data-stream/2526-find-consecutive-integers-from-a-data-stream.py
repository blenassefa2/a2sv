class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.qu = deque()
        self.numOfValue = 0
        

    def consec(self, num: int) -> bool:
        if len(self.qu) == self.k:
            if self.qu.popleft() == self.value:
                self.numOfValue -= 1
        self.qu.append(num)
        if num == self.value:
            self.numOfValue += 1
        if self.numOfValue == self.k:
            return True
        return False 


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)