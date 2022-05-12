class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split("/")
        
        canonical = ["/"]
        for i in p:
            if i != "." and i != "":
                if i != "..":
                    canonical.append(i)
                    canonical.append("/")
                else:
                    if len(canonical) >= 3:
                        canonical.pop()
                        canonical.pop()
                    elif len(canonical) == 2:
                        canonical.pop()
        if len(canonical) > 1:
            canonical.pop()
            return "".join(canonical)
                        
        return "/"