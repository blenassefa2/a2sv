class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        def dp(i, prev,store):
            
            if i >= len(s):
                return 0
            
            if (i,prev) in store:
                return store[(i,prev)]
            curr = s[i]
            currChange = "1"
            if curr == currChange:
                currChange = "0"
            
            changed , unchanged = inf, inf
            
            if prev == "0":
                changed = dp(i + 1, currChange, store) + 1
                unchanged = dp(i + 1, curr, store)
            else:
                if curr == "0":
                    changed = dp(i + 1,currChange, store) + 1
                else:
                    unchanged = dp(i + 1, curr, store)
            store[(i,prev)] = min(changed, unchanged)
            return store[(i,prev)]
        return dp(0,"0", defaultdict(int))