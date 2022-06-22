class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       
        heapify(nums)
        t = 0
        for i in range(len(nums) + 1 - k):
            t = heappop(nums)
        return t
            