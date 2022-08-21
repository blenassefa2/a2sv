class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = set()
        candidates.sort()
        """
        recursive function
        
        Args:
        ----
            curr_sum
            curr_index
            curr_path
        base: if curr_index >= len(cadidates)
              if cur_sum == target
        """
        def recurs(curr_sum, curr_index, curr_path, visited):
            # print(curr_path)
            if curr_path in visited:
                return
            if curr_index >= len(candidates):
                return
            if curr_sum == target:
                
                self.ans.add(tuple(curr_path))
                return
            if curr_sum > target:
                return
            visited.add(curr_path)
            for i in range(curr_index + 1, len(candidates)):
                new_path = curr_path
                new_path += (candidates[i],)
                new_sum = curr_sum + candidates[i]
                
                recurs(new_sum, i, new_path, visited)
                
                
        """Driver code"""
        visited = set()
        
        for j in range(len(candidates)):
            if (candidates[j],) not in visited:
                recurs(candidates[j], j, (candidates[j],), visited)
            
        return self.ans