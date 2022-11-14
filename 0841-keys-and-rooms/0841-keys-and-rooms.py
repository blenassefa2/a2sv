class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        I think this is simple bfs I go from each room to the other rooms of which I have their key
        """
        
        qu = deque([0])
        visited = set()
        while qu:
            
            N = len(qu)
            
            for _ in range(N):
                room = qu.popleft()
                
                if room in visited:
                    continue
                
                visited.add(room)
                
                for keys in rooms[room]:
                    qu.append(keys)
        
        return len(visited) == len(rooms)