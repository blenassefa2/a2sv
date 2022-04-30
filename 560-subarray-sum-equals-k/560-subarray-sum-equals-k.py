class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prevSum = defaultdict(lambda : 0)

        res = 0

        # Sum of elements so far.
        currsum = 0

        for i in range(0, len(nums)):

            # Add current element to sum so far.
            currsum += nums[i]

            # If currsum is equal to desired sum,
            # then a new subarray is found. So
            # increase count of subarrays.
            if currsum == k:
                res += 1		

            # currsum exceeds given sum by currsum - sum.
            # Find number of subarrays having
            # this sum and exclude those subarrays
            # from currsum by increasing count by
            # same amount.
            if (currsum - k) in prevSum:
                res += prevSum[currsum - k]


            # Add currsum value to count of
            # different values of sum.
            prevSum[currsum] += 1

        return res