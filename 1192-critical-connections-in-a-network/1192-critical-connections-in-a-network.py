
class Solution:
    def criticalConnections(self, n, connections):
        # init graph
        graph = defaultdict(set)
        for fr, to in connections:
            graph[fr].add(to)
            graph[to].add(fr)

        # backtracking
        steps, crit_conn = [None] * n, []

        def dfs(fr, parrent):
            min_step = n

            for to in graph[fr]:
                if to == parrent: continue

                if steps[to] is None:
                    steps[to] = steps[fr] + 1
                    dfs(to, fr)

                min_step = min(min_step, steps[to])

            if min_step < steps[fr]:
                # steps[fr] is too big, we can reach current vertex from a better step : min_step
                steps[fr] = min_step
            else:
                # steps[fr] is the best we can get from parrent, so it's not in a loop, (parrent, fr) is a BIRDGE
                if parrent != -1: crit_conn.append([fr, parrent])

        steps[0] = 0
        dfs(0, -1)  # dummy parrent -1

        return crit_conn