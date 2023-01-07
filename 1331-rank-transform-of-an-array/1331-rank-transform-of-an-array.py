class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
        I will sort the array and find out the # of values greater than each value then construct the answer
        TC = nlogn
        SC = n
        """
        
        
        #initialize variables:
        lessThanMe = defaultdict(int)
        answer = [value for value in arr]
        index = 0
        
        # update the lessThanMe dictionary
        arr.sort()
        for i, value in enumerate(arr):
            if value not in lessThanMe:
                lessThanMe[value] = index + 1
                index += 1
            else:
                lessThanMe[value] = index
                
                
        # build your answer
        for index, value in enumerate(answer):
            answer[index] = lessThanMe[value]

        
        #return the answer
        return answer