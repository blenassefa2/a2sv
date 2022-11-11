class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        validChars = set()
        if name[0] != typed[0]:
            return False
        for i in name:
            validChars.add(i)
        
        counter1 = 0
        counter2 = 0
        while counter2 < len(typed) :
            if typed[counter2] not in validChars:
                return False
            
            if name[counter1] == typed[counter2]:
                counter1 += 1   
            else:
                 if counter1 > 0 and name[counter1 -1] != typed[counter2]:
                        break
            if counter1 == len(name):
                break
            counter2 += 1
       
        if counter1 != len(name):
            return False
        for index in range(counter2, len(typed)):
            if name[counter1-1] != typed[index]:
                return False
        
        return True