class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        """
        for this questions since we can move the ones in any way we can 
        
        we only need to check if number of ones are equal or not
        and the number ones and the minimum of the two will be the answer
        
        """
        R = len(img1)
        C = len(img1[0])        

        def calc_overlap(dr, dc, img1, img2):
            ans1 = ans2 = 0
            for r in range(R):
                for c in range(C):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        # res[nr][nc] = img1[r][c]
                        if img1[nr][nc] == 1 and img1[nr][nc] == img2[r][c]:
                            ans1 += img1[nr][nc]
                        if img2[nr][nc] == 1 and img2[nr][nc] == img1[r][c]:
                            ans2 += img2[nr][nc]                            
                    else:
                        break
            return max(ans1, ans2)
        ans = 0

        for r in range(0, R):
            for c in range(0, C):
                for dr, dc in ((r,c), (r,-c), (r,c), (-r,c)):
                    # img3 = translate(dr, dc, img1)                    
                    ans = max(ans, calc_overlap(dr, dc, img1, img2))

        return ans