class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        root = [i for i in range(len(accounts))]
        dicit = defaultdict(int)
        def find(node):
            if root[node] == node:
                return node
            root[node] = find(root[node])
            return root[node]
            
        def union(parent,child):
            ro_p = find(parent)
            ro_c = find(child)
            if ro_p != ro_c:
                root[ro_c] = ro_p
            
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                if accounts[i][j] not in dicit:
                    dicit[accounts[i][j]] = i
                else:
                    union(dicit[accounts[i][j]],i)

        dic_2 = defaultdict(list)
        
        for i in range(len(root)):
            for email in dicit:
                if i == dicit[email]:
                    dic_2[find(root[i])].append(email)
        res = []
        for key in dic_2:
            res.append([accounts[key][0]])
            res[-1].extend(sorted(dic_2[key]))
        return res