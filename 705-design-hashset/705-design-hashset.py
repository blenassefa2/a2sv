class MyHashSet:

    def __init__(self):
        self.hash = defaultdict()

    def add(self, key: int) -> None:
        self.hash[key] = 1

    def remove(self, key: int) -> None:
        if key in self.hash:
            self.hash.pop(key)

    def contains(self, key: int) -> bool:
        if key in self.hash:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)