class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer = [0]
        answer.extend(digits)
        carry = 1
        digit = len(answer) -1
        while carry != 0:
            prev = answer[digit]
          
            answer[digit] = (prev + 1)% 10
            carry = (prev + 1) // 10
            digit -= 1
            
        if answer[0] ==0:
            return answer[1:]
        return answer 