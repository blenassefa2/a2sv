class RandomizedCollection:

    def __init__(self):
        self.index = defaultdict(set)
        self.array = []

    def insert(self, val: int) -> bool:
        found = True
        if val in self.index:
            found = False
        self.index[val].add(len(self.array))
        self.array.append(val)
        return found

    def remove(self, val: int) -> bool:
       
        if val in self.index:
            
            nw = self.array[-1]
            if nw == val:
                self.index[val].remove(len(self.array)-1)
            else:
                idx = self.index[val].pop()

                self.array[idx] = nw
                self.index[nw].remove(len(self.array)-1)
                self.index[nw].add(idx)

            self.array.pop()
            if len(self.index[val]) == 0:
                self.index.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.array)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()