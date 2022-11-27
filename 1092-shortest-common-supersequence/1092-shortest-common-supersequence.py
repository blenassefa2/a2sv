


INT_MAX = 1000000
big_string = "*"*INT_MAX
class Solution:
    # __count = 0
    __str1 = None
    __str2 = None
    @lru_cache(maxsize=100000)
    def helper(self, pointer1: int, pointer2: int):
        # Solution.__count += 1
        # print(Solution.__count)
        # handle the base case
        if pointer1 >= len(Solution.__str1) and pointer2 >= len(Solution.__str2):
            return ""
        
        
        # if pointer1 and pointer2 both have same value
        if pointer1 < len(Solution.__str1) and pointer2 < len(Solution.__str2) and Solution.__str2[pointer2] == Solution.__str1[pointer1]:
            return self.helper(pointer1 + 1, pointer2 + 1)+ Solution.__str2[pointer2]
             
            
            
        pick_1, pick_2 = big_string, big_string
        # pick one
        if pointer1 < len(Solution.__str1):
            pick_1 = self.helper(pointer1+1, pointer2) + Solution.__str1[pointer1]
        
        # pick two
        if pointer2 < len(Solution.__str2):
            pick_2 =  self.helper(pointer1, pointer2 + 1) + Solution.__str2[pointer2]
        
        # return minimum length
        return min(pick_1, pick_2, key=lambda x: len(x))
        
    
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # print(len(str1),len(str2))
        Solution.__str1 = str1
        Solution.__str2 = str2
        return self.helper(0,0)[::-1]
