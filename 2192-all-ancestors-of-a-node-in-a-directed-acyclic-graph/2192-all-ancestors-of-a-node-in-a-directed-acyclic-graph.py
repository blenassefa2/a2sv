class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        dict_ = defaultdict(list)
        parent = [0]*n
        ans =  defaultdict(set)
        
        
        for head,tail in edges:
            dict_[head].append(tail)
            parent[tail] += 1
            
            
        q = deque()
        for j in range(n):
            if not parent[j]:
                q.append(j)
      
        while q:
            curr = q.popleft()
             
            for i in dict_[curr]:
           
                parent[i] -= 1

                ans[i].add(curr)
                ans[i] = set().union(ans[curr], ans[i])
                if not parent[i]:
                    q.append(i)
            # print(q)
        final = [[]]*n
        
        for k in ans:
            final[k] = sorted(list(ans[k]))
        return final