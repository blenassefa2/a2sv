class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        This looks like a straight forward bfs
        
        we can travel from one route to other routes
        
        at every level we are going to ask which bus should I get in too given my current route
        
        if the current bus we are in containes the target route then we've finished travelling
        
        if we exhaust all buses but we didn't reach our target then return -1
        
        """
        # edge case
        if source == target:
            return 0
        
        # initialize variables
        qu = deque([])
        buses = defaultdict(set)
        visitedBus = set()
        
        # construct the buses
        for i in range(len(routes)):
            buses[i] = set(routes[i])
            
        
        # populate the queue
        for i in buses:
            if source in buses[i]:
                qu.append([i, 1])
                if target in buses[i]:
                    return 1
        
        # proceed with the bfs
        while qu:
            bus, length = qu.popleft()
            
            if target in buses[bus]:
                return length
            
            if bus in visitedBus:
                continue
            visitedBus.add(bus)
            
            for route in routes[bus]:
                
                for i in buses:
                    if route in buses[i]:
                        qu.append([i, length + 1])
        return -1