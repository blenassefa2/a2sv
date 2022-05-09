class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        a = len(nums1)//2
        if n %2 == 1:
            return nums1[a]
        else:
            return (nums1[a] +nums1[a-1])/2