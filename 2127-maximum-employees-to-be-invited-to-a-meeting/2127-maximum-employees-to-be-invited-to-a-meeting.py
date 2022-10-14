class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        self.cycle = []
        
        twos = defaultdict()
        t= 0
        incoming = defaultdict(list)
        for i in range(len(favorite)):
            if favorite[favorite[i]] != i:
                incoming[favorite[i]].append(i)
        self.visited = set() 
        def find(node):
            ans = 0
            self.visited.add(node)
            for i in incoming[node]:
                ans = max(ans, find(i))
            return ans + 1
               
        def has_cycle(node,grey):
            if node in grey:
                
                self.cycle.append([len(grey),node])
                return
            self.visited.add(node)
            grey.add(node)
            has_cycle(favorite[node],grey)
            grey.remove(node)
        l = 0
        prev = 0
        t = 0
        for i in range(len(favorite)):
            
            if i not in self.visited:
                has_cycle(i,set())
                a,b = self.cycle[-1]
               
                x = favorite[b]
                c = 1
                while x != b:
                    x = favorite[x]
                    c+=1
                if c > 2:
                    a = c
                else:
                    
                    a = 0
                    sub = 0
                    d = tuple(sorted([favorite[b],b]))
                    
                    k = find(b) + find(favorite[b])
                    
                    if d not in twos:
                        t += k
                    twos[d] = k
                    
                    a += t
                    
                        
                    
                # print(twos)
                l = max(l,a)
        
        return l