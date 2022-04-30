class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = deque(sorted(nums1))
        n2 = deque(sorted(nums2))
        ans = []
        while n1 and n2:
            if n1[0] == n2[0]:
                ans.append(n1[0])
                n1.popleft()
                n2.popleft()
            elif n1[0] > n2[0]:
                n2.popleft()
            elif n1[0] < n2[0]:
                n1.popleft()
        return(ans)