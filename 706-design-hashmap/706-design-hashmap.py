class MyHashMap:

    def __init__(self):
        self.dict_ = defaultdict() 

    def put(self, key: int, value: int) -> None:
        self.dict_[key] = value

    def get(self, key: int) -> int:
        if key not in self.dict_:
            return -1
        return self.dict_[key]

    def remove(self, key: int) -> None:
        if key in self.dict_:
            self.dict_.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)