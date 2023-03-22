class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = defaultdict(int)
        target = defaultdict(int)
        left = 0
        right = 0
        matched = False
        
        # build target
        for char in s1:
            target[char] += 1
            
        
        # move window while checking if condition satisfied
        while right < len(s2):
            if right == left and s2[right] not in target:
                right += 1
                left += 1
                continue
            
            if window[s2[right]] + 1 <= target[s2[right]]:
                window[s2[right]] += 1
                right += 1
            else: 
                window[s2[left]] -= 1
                left += 1
                
            matched = True
            for char in "abcdefghijklmnopqrstuvwxyz":
                if window[char] != target[char]:
                    matched = False
                    
            if matched:
                return True
        return False