
class Solution:
    def find_root(self,node,parent):
        if parent[node] == node:
            return node
        
        parent[node] = self.find_root(parent[node],parent)
        return parent[node]
    
    def union(self, node1,node2,rank,parent):
        node1_parent =self.find_root(node1,parent)
        node2_parent =self.find_root(node2,parent)
        if node1_parent == node2_parent:
            return False
        if rank[node1_parent] > rank[node2_parent]:
            parent[node2_parent] = node1_parent
            rank[node1_parent] += 1
        else: 
            parent[node1_parent] = node2_parent
            rank[node1_parent] += 1
        return True

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # initialize the necessary storage for the union find 
        parent = [i for i in range(len(edges)+1)]
        size = [1]* (len(edges)+1)
        
        # for every edge uniify the nodes
        for node1,node2 in edges:
        
            if not self.union(node1,node2,size,parent):
                return [node1,node2]
            
            
        
        
        
        