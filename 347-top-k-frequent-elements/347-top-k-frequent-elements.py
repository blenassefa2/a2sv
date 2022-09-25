class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        crev = defaultdict(list)
        c = [0] *(max(counts.values())+1)
        
        for n in counts:
            crev[counts[n]].append(n)
            c[counts[n]] += 1
            # c[counts[n]][/1].append(n)
        sum_ = 0
        ans = []
        for i in range(len(c) -1, -1, -1):
            if sum_ >= k:
                break
            ans.extend(crev[i])
            sum_ += c[i]
        
        return ans
            