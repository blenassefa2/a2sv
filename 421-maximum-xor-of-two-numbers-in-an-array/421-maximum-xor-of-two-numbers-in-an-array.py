class Node:
    def __init__(self):
        self.children = defaultdict(str)
        self.end = False
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, binary: str) -> None:
        current = self.root
        
        for b in binary:
            if b not in current.children:
                current.children[b] = Node()
            current = current.children[b]
        current.end = True
    def search(self, binary, st) -> str:
        current = self.root
        ret = ""
        
        for j in range(0, st):
            current = current.children["0"]
   
        for i in range(st, len(binary)):
            b = "1" if binary[i] == "0" else "0"
            c = binary[i]
            if b  in current.children:
                ret += b
                current = current.children[b]
            else:
                ret += c
                current = current.children[c]
        return ret
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        nums.sort()
        new = Trie()
        max_ = len(bin(nums[-1])[2:])
        for i in range(len(nums) - 1, -1,-1):
            new.insert(f'{nums[i]:032b}')
        
        ans = nums[-1] ^nums[0]
        
        for i in nums:
            b = int(new.search(f'{i:032b}', 32 - max_), 2)
            ans = max(ans, b ^ i)
        
        return ans
        
        