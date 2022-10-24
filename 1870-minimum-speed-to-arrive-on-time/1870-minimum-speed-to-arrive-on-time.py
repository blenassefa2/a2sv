class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def calculator(array, speed):
            total = 0
            for i in range(len(array)):
                if i == len(array) -1:
                    total +=  array[i] / speed
                else:
                    total +=  ceil(array[i] / speed)
            return total


        # initialize my left right varibles
        left, right = 1, 10**7
        best =  -1
        while left <= right:
            mid = (left+right) //2
            ans = calculator(dist, mid)

            if ans > hour:
                left = mid + 1
            else:
                best = mid
                right = mid - 1
        return best