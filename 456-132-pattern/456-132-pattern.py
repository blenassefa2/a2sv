class Solution:
	def find132pattern(self, nums: List[int]) -> bool:
		nums_len = len(nums)
		if nums_len <= 2:
			return False
		left_min_list = [nums[0]]
		for i in range(1, nums_len): 
			if nums[i]<left_min_list[i-1]:
				left_min_list.append(nums[i]) 
			elif nums[i]>=left_min_list[i-1]: 
				left_min_list.append(left_min_list[i-1]) 

		stack = list()
		for i in range(nums_len-1,-1,-1): 
			if nums[i]>left_min_list[i]:
				while len(stack)>0 and stack[-1]<=left_min_list[i]: 
					stack.pop()
				if len(stack)>0 and stack[-1]<nums[i]:
					return True
				stack.append(nums[i])
		return False