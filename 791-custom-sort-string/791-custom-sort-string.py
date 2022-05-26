class Solution:
    def customSortString(self, order: str, s: str) -> str:
        check = defaultdict(int)
        for i in range(len(order)):
            check[order[i]] = i + 1
        s = list(s) 
        s.sort(key =lambda x: check[x])
        return ("".join(s))