class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        pos_sup = set(recipes)
        supp = set(supplies)
        def possible (r,visited,dp):
            ans = True
            visited.add(recipes[r])
            if r in dp:
                return dp[r]
            for i in ingredients[r]:
                if i in supp:
                    ans = ans and True
                elif i in pos_sup:
                    if i in visited:
                        return False
                    ans = ans and possible(recipes.index(i),visited,dp)
                else:
                    ans = ans and False
            dp[r] = ans
            return dp[r]
        
        final = []
        d = defaultdict(bool)
        for x in range(len(recipes)):
            if possible(x,set(),d):
                final.append(recipes[x])
        return final
        