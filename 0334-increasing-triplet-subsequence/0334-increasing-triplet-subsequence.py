class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        # initialize my variables
        isValid = False
        maximums = [nums[-1]] # [4]
        stack = []

        # Building my maximums
        for index in range(len(nums)-2, -1, -1):
            maximums.append(max(maximums[-1], nums[index]))

        maximums.reverse()

        # traverse check if I can have valid combinations
        index = 0
        while index < len(nums):

            if not stack:
                stack.append(index)
                index += 1
            else:
                if nums[stack[-1]] >= nums[index]:
                    stack.pop()
                else:
                    if maximums[index] > nums[index]:
                        isValid = True
                    index += 1


        # return final answer
        return isValid