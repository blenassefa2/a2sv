class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x = 0
        for j in range(m, m+ n):
            nums1[j] = nums2[x]
            x += 1
        nums1.sort()