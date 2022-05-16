class Solution:
	def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
		if grid[0][0] or grid[-1][-1]:
			return -1

		n = len(grid)
		if n == 1:
			return 1

		queue = deque([(0, 0, 1)])

		def allowed_dirs(i, j):
			output = [] 
			for x in range(i + 1, i - 2, -1): #why not?
				for y in range(j + 1, j - 2, -1):
					if 0 <= x < n and 0 <= y < n and not grid[x][y]:
						output.append((x, y))
			return output

		grid[0][0] = 1

		while queue:
			i, j, cur = queue.popleft()
			cur += 1
			for x, y in allowed_dirs(i, j):
				grid[x][y] = 1 #there is no way back\U0001f642
				if x == y == n - 1:
#we do not need to compare with other paths because we move between levels with the same number of visited cells:
					return cur
				else:
					queue.append((x, y, cur))
		return -1