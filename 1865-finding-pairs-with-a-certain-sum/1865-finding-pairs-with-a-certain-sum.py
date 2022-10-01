class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = Counter(nums1)
        self.nums = Counter(nums2)
        self.numslt = nums2
        

    def add(self, index: int, val: int) -> None:
        self.nums[self.numslt[index]] -=1
        if self.nums[self.numslt[index]] <= 0:
            self.nums.pop(self.numslt[index])
        self.numslt[index] += val
        self.nums[self.numslt[index]] += 1

    def count(self, tot: int) -> int:
        c = 0
        for i in self.nums1:
            if tot - i in self.nums:
                c += (self.nums1[i]*self.nums[tot-i])
        return c


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

"""
I am going to build two normal lists and two dictionaries

so that when I am asked the count query
    I iterate through one of the dictionaries 
    search the target - i in the other dictionary:
    and add the count according to the counts of i and target -i
    
when the query is add:
    I change the index accordingly and update the dictionary

"""