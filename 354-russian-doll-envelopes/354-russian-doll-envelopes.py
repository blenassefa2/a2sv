class Solution:
    def maxEnvelopes(self, e: List[List[int]]) -> int:
        def cmpfunc(x, y):
            if x[0] == y[0]:
                if y[1] > x[1]:
                    return 1
                return -1
            if x[0] > y[0]:
                return 1
            return -1

        def lenLIS(arr):
            def lb(x):
                l, r = 0, len(lis)-1
                while l <= r:
                    m = l+(r-l)//2
                    if e[lis[m]][1] >= x:
                        r = m-1
                    else:
                        l = m+1
                return l
                                
            lis = []
            for i in range(len(arr)):
                x = lb(arr[i][1])
                if x >= len(lis):
                    lis.append(i)
                else:
                    lis[x] = i
            return len(lis)
        
        e.sort(key=functools.cmp_to_key(cmpfunc))
        return lenLIS(e)