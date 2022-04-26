class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        root = [i for i in range(n + 1)]
        rank = [0]*(n+1)
        def find(x):
            if root[x] == x:
                return x
            root[x] = find(root[x])
            return root[x]
        def union(i,j):
            a,b = find(i), find(j)
           
            if a == b:
                return False
            
            if rank[a] > rank[b]:
                root[b] = root[a]
                rank[a] += rank[b]
            else:
                root[a] = root[b]
                rank[b] += rank[a]
            
            return True                                       
        
        for i in edges:
            a = union(i[0],i[1])
       
            if not a:
                return i
        print(root) 
        